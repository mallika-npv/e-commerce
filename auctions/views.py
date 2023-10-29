from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Catagory, Listing, Comments, Bid

def index(request):
    active = Listing.objects.filter(is_active = True)
    allcat = Catagory.objects.all()
    return render(request, "auctions/index.html",{
        "listings" : active,
        "cats" : allcat
    })

def watchlist(request):
    curr_user = request.user
    items = curr_user.watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "listings" : items
    })

def addb(request, id):
    if request.method == "POST":
        new_bid = float(request.POST['new_bid'])
        item = Listing.objects.get(pk=id)
        if new_bid > item.price.bid:
            ubid = Bid(bid = new_bid, user=request.user)
            ubid.save()
            item.price = ubid
            item.save()
            return render(request, "auctions/listing.html",{
                "item" : item,
                "is_note" : True
            })
        else:
            return render(request, "auctions/listing.html",{
                "item" : item,
                "is_note" : False
            })

def addc(request, id):
    curr_user = request.user
    listings = Listing.objects.get(pk=id)
    message = request.POST['new_comment']
    new = Comments(
        author = curr_user,
        listing = listings,
        message = message 
    )
    new.save()
    return HttpResponseRedirect(reverse(listing, args=(id, ))) 

def removew(request, id):
    if request.method == "POST":
        item = Listing.objects.get(pk=id)
        curr_user = request.user
        item.watchlist.remove(curr_user)
        return HttpResponseRedirect(reverse(listing, args=(id, )))

def addw(request, id):
    if request.method == "POST":
        item = Listing.objects.get(pk=id)
        curr_user = request.user
        item.watchlist.add(curr_user)
        return HttpResponseRedirect(reverse(listing, args=(id, )))

def listing(request, id):
    item = Listing.objects.get(pk=id)
    all_comments = Comments.objects.filter(listing = item)
    in_watchlist = request.user in item.watchlist.all()
    is_owner = request.user.username == item.owner.username
    return render(request, "auctions/listing.html",{
        "item" : item,
        "in_watchlist" : in_watchlist,
        "all_comments" : all_comments,
        "is_owner" : is_owner
    })

def close(request, id):
    is_owner = request.user.username == item.owner.username
    item = Listing.objects.get(pk=id)
    item.is_active = False
    item.save()
    return render(request, "auctions/listing.html",{
        "item" : item,
        "is_owner" : is_owner
    })

def display(request):
    if request.method == "POST":
        catagory = Catagory.objects.get(cat_name = request.POST['catagory'])
        active = Listing.objects.filter(is_active = True, catagory = catagory)
        allcat = Catagory.objects.all()
        return render(request, "auctions/index.html",{
            "listings" : active,
            "cats" : allcat
        })

def create_listing(request):
    if request.method == "GET":
        allcat = Catagory.objects.all()
        return render(request, "auctions/create.html",{
            "cats" : allcat
        })
    else:
        title = request.POST["title"]
        describtion = request.POST["describtion"]
        img_url = request.POST["img_url"]
        price = float(request.POST["price"])
        curr_user = request.user
        catagory = Catagory.objects.get(cat_name = request.POST["catagory"])
        
        bid = Bid(bid=price, user=curr_user)
        bid.save()

        new = Listing(
            title = title, describtion = describtion,
            img_url = img_url, price = bid, catagory = catagory,
            owner = curr_user
        )
        new.save()
        return HttpResponseRedirect(reverse(index))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

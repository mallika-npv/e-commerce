from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Catagory(models.Model):
    cat_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.cat_name

class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid", blank=True, null=True)

class Listing(models.Model):
    title = models.CharField(max_length=30)
    describtion = models.CharField(max_length=300)
    img_url = models.CharField(max_length=1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="bids", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", blank=True, null=True)
    catagory = models.ForeignKey(Catagory, blank=True, null=True, on_delete=models.CASCADE, related_name="catagory")
    watchlist = models.ManyToManyField(User, null=True, blank=True, related_name="watchlist")

    def __str__(self) -> str:
        return self.title
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_c", blank=True, null=True)
    message = models.CharField(max_length=200)

from django.contrib import admin
from .models import User, Listing, Catagory, Comments, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Catagory)
admin.site.register(Comments)
admin.site.register(Bid)
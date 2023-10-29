from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("display", views.display, name="display"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removew/<int:id>", views.removew, name="removew"),
    path("addw/<int:id>", views.addw, name="addw"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addc/<int:id>", views.addc, name="addc"),
    path("addb/<int:id>", views.addb, name="addb"),
    path("close/<int:id>", views.close, name="close"),
]

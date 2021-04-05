from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=100,default='username')


class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bid")

    def __str__(self):
        return f"{self.user} - ${self.bid}"


class Listing(models.Model):
    title = models.CharField(max_length=32)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listing", null=True, blank=True)
    is_closed = models.BooleanField(default=False, blank=True, null=True)
    description = models.CharField(max_length=400)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE,
                            related_name="listing", default=None)
    url = models.CharField(max_length=800,default="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",null=True, blank=True)
    watchlist = models.ManyToManyField(
        User, blank=True, related_name="watch_listings")
    category = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.category}"


class Comment(models.Model):
    text = models.CharField(max_length=800)
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="comments")

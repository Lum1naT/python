from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=9999)
    email = models.EmailField(max_length=254)
    account_status = models.PositiveIntegerField(default=1)
    account_created = models.DateTimeField('date published')

    def __str__(self):
        return self.username


class Entry(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=254)
    content = models.TextField()
    times_liked = models.PositiveIntegerField(default=0)
    times_disliked = models.PositiveIntegerField(default=0)
    date_posted = models.DateTimeField('date published')

class Comment(models.Model):
    entry_fk = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    date_posted = models.DateTimeField('date published')
    times_liked = models.PositiveIntegerField(default=0)
    times_disliked = models.PositiveIntegerField(default=0)

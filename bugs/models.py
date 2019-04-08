from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Bugs(models.Model):
    """ A Single Bug model"""

    STATUS_CHOICES = (
        ('Waiting', 'Waiting'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed')
    )

    title = models.CharField(
        max_length=200
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=('Waiting', 'Waiting')
    )
    content = models.TextField()
    username = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        blank=True, default=timezone.now, null=True
    )
    published_date = models.DateTimeField(
        auto_now_add=True
    )
    start_date_for_fixing = models.DateTimeField(
        blank=True, default=None, null=True
    )
    fixed_date = models.DateTimeField(
        blank=True, default=None, null=True
    )
    views = models.BigIntegerField(default=0)
    tag = models.CharField(
        max_length=30, blank=True, null=True
    )
    image = models.ImageField(
        upload_to="img", blank=True, null=True
    )
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comments(models.Model):
    """ Comment model that is connected with Bugs
    and username that is creating a comment"""
    ticket = models.ForeignKey(
        Bugs, null=True, on_delete=models.CASCADE
    )
    username = models.ForeignKey(
        User, null=None, on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    comment = models.TextField(
        blank=False
    )

    def __str__(self):
        return self.comment


class BugsUpvote(models.Model):
    """ List of upvoted bugs """
    upvoted_bug = models.ForeignKey(Bugs, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

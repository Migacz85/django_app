from django.db import models


class Bugs(models.Model):
    """ A Single Bug model"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)


    def __unicode__(self):
        return self.title



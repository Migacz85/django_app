from django.db import models
from django.contrib.auth.models import User

class ProfilePic(models.Model):
    avatar = models.ImageField(
        upload_to='img', blank=True
    )
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.picture)

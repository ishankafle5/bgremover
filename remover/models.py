from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=255)


class ImageDetails(models.Model):
    image_year = models.DateTimeField(datetime.now().year)
    image_month = models.DateTimeField(datetime.now().month)
    image_day = models.DateTimeField(datetime.now().day)
    image_name = models.CharField(max_length=255, blank=True)
    image_link = models.CharField(max_length=255, blank=True)
    remove_name = models.CharField(max_length=255, blank=True)
    remove_link = models.CharField(max_length=255, blank=True)

    user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return super().image_name, super().image_link

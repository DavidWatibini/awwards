from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Image(models.Model):

    image_name = models.CharField(max_length=50, blank=True)
    image_view = models.ImageField(upload_to = 'gallery/')
    image_description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=50, blank=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_description

    def save_image(self):
        self.save()

    def set_description(self,new_description):
        self.description = new_description
        self.save()


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts=models.CharField(max_length=50, blank=True)
    website=models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.contacts

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

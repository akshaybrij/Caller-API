from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    full_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True)
    num =  models.CharField(unique=True,null=False,blank=False,max_length=10,help_text='Contact number Please')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name','num']


    def get_full_name(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=100,blank=True)
    num = models.CharField(max_length=12,null=False,blank=False,help_text='Contact number')
    spam = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_profile_contact(sender,instance,created,**kwargs):
    if created:
        Contact.objects.create(full_name=instance.full_name,num=instance.num)

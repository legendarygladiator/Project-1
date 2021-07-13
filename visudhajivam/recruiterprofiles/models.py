from django.contrib.auth.models import AbstractUser
from home.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


# class Organization(models.Model):
    
#     amount = models.IntegerField(default=0)
#     name = models.CharField(max_length=90)
#     email = models.CharField(max_length=111, default="")
#     phone = models.CharField(max_length=12, default="")
#     image = models.ImageField(upload_to='images' )
#     timeStamp = models.DateTimeField(default=now)

class Mypostjob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=500,default="")
    experience = models.CharField(max_length=5000,default="")
    package = models.CharField(max_length=500,default="")
    location = models.CharField(max_length=500,default="")
    skill= models.CharField(max_length=500,default="")
    desc = models.CharField(max_length=5000,default="")
    pub_date = models.DateField(default=now)




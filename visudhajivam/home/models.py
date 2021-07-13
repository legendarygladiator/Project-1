from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


    def __str__(self):
        return self.username

class Student(models.Model):
    myuser = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
   
    users = models.CharField(max_length=12, default="")
    first_name = models.CharField(max_length=12, default="")
    last_name = models.CharField(max_length=12, default="")
    country = models.CharField(max_length=12, default="")
    city = models.CharField(max_length=12, default="")
    state = models.CharField(max_length=12, default="")
    institution= models.CharField(max_length=20, default="")
    qualification= models.CharField(max_length=90,default="")
    address = models.CharField(max_length=111, default="")
    contact = models.CharField(max_length=12, default="")
    email = models.CharField(max_length=20, default="")
    skills = models.CharField(max_length=20, default="")
    zipcode =  models.CharField(max_length=12, default="")
    DOB = models.DateField(default=now)
    timeStamp = models.DateTimeField(default=now)
    


    


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111, default="")
    phone = models.CharField(max_length=12, default="")
    image = models.ImageField(upload_to='images' )
    timeStamp = models.DateTimeField(default=now)




class Myinfo(models.Model):
    
    users = models.CharField(max_length=12, default="")
    first_name = models.CharField(max_length=12, default="")
    last_name = models.CharField(max_length=12, default="")
    country = models.CharField(max_length=12, default="")
    city = models.CharField(max_length=12, default="")
    state = models.CharField(max_length=12, default="")
    institution= models.CharField(max_length=20, default="")
    qualification= models.CharField(max_length=90,default="")
    address = models.CharField(max_length=111, default="")
    contact = models.CharField(max_length=12, default="")
    email = models.CharField(max_length=20, default="")
    skills = models.CharField(max_length=20, default="")
    zipcode =  models.CharField(max_length=12, default="")
    DOB = models.DateField(default=now)
    job_id = models.IntegerField(default=0)
   
    def __str__(self):
       return  self.users
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=55)
    roll = models.IntegerField()
    email = models.EmailField(max_length=255)

class Address(models.Model):
    house_no = models.IntegerField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=50)

class Detail(models.Model):
    username = models.CharField(max_length=50)
    dob = models.IntegerField()
    age = models.IntegerField()
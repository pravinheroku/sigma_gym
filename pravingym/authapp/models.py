from ast import mod
from operator import truediv
from pyexpat import model
from turtle import mode
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.email


class Enrollment(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField()
    gender = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)
    dob = models.DateField()
    select_membership_plan = models.CharField(max_length=200)
    select_trainer = models.CharField(max_length=55)
    reference = models.CharField(max_length=55)
    address = models.TextField()
    payment_status = models.CharField(max_length=55, blank=True, null=True)
    payment_amount = models.IntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    salary = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField()

    def __str__(self):
        return self.plan


class GALLERY(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="gallery")
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    phonenumber = models.CharField(max_length=15)
    Selectdate = models.DateField(auto_now_add=True)
    Login = models.CharField(max_length=200)
    Logout = models.CharField(max_length=200)
    SelectWorkout = models.CharField(max_length=200)
    TrainedBy = models.CharField(max_length=200)

    def __int__(self):
        return self.id

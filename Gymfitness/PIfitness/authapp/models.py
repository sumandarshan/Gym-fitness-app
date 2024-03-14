from django.db import models
from django.conf import settings


class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    def __int__(self):
        return self.id

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length = 12)
    description = models.TextField()

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    Fullname=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=10)
    Phonenumber=models.CharField(max_length=12)
    DOB=models.DateField(auto_now=False, auto_now_add=False)  #auto_now and auto_now_add will prevent automatic submission of today's date
    SelectMembershipPlan=models.CharField(max_length=180)
    SelectTrainer=models.CharField(max_length=50)
    Reference=models.CharField(max_length=25)
    Address=models.TextField()
    Paymentstatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.Fullname
    
class Trainer(models.Model):
    name=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phonenumber=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField(max_length=45)
    def __int__(self):
        return self.id
    
    # id is default primary key for all the tables


class WorkoutLog(models.Model):
    Selectdate = models.DateTimeField(auto_now_add=True)
    Fullname = models.CharField(max_length=255)
    Login = models.CharField(max_length=200)
    Logout = models.CharField(max_length=200)
    SelectWorkout = models.CharField(max_length=200)
    w1 = models.CharField(max_length=200, default='')
    r1 = models.CharField(max_length=200, default='')
    w2 = models.CharField(max_length=200, default='')
    r2 = models.CharField(max_length=200, default='')
    w3 = models.CharField(max_length=200, default='')
    r3 = models.CharField(max_length=200, default='')
    TrainedBy = models.CharField(max_length=200)
    mail = models.EmailField(default=settings.DEFAULT_FROM_EMAIL)
    def __int__(self):
        return self.id





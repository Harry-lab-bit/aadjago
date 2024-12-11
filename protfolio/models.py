from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15, null=True, blank=True)  # Allow NULL for phone number
    description = models.TextField(null=True, blank=True)  # Allow NULL for description

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    authname = models.CharField(max_length=15)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def  __str__(self):
        return self.title
    
class Internship(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    usn = models.CharField(max_length=20)
    college_name = models.CharField(max_length=100)
    offer_status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    proj_report = models.TextField(null=True, blank=True)  # Allow NULL and blank values


    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.usn
    
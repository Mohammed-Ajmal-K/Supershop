from django.db import models

# Create your models here.
class registrationdb(models.Model):

    Uname=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Uimg",null=True,blank=True)

class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)


class cartdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to="Product",null=True,blank=True)

class checkoutdb(models.Model):
    Country=models.CharField(max_length=100,null=True,blank=True)
    Fname=models.CharField(max_length=100,null=True,blank=True)
    Lname=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    Zip=models.IntegerField(null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
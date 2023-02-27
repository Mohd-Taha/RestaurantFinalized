from django.db import models

# # Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20,default="")
    salary = models.IntegerField(default="0")   
    Face_book = models.CharField(max_length=30,default="")
    Twitter = models.CharField(max_length=30,default="")
    Instagram = models.CharField(max_length=30,default="")
    image = models.ImageField(upload_to="img")


class order(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    img= models.ImageField(upload_to="img")

class testimonial(models.Model):
    imagee = models.ImageField(upload_to="img")
    name:models.CharField(max_length=25)
    review = models.CharField(max_length=300)

class featured(models.Model):
    picture = models.ImageField(upload_to="img")
    dish_name=models.CharField(max_length=25)
    dish_price = models.IntegerField()
    

class starters(models.Model):
    pic = models.ImageField(upload_to="img")
    starter_name =models.CharField(max_length=20)
    starter_desc =models.CharField(max_length=50)
    starter_price=models.IntegerField()

class products(models.Model):
     pict = models.ImageField(upload_to="img")
     pro_name=models.CharField(max_length=20)
     pro_desc =models.CharField(max_length=600)
     pro_price=models.IntegerField()
     pro_reviews=models.CharField(max_length=200)

from django.db import models

# Create your models here.
class poto(models.Model):
    nme= models.CharField(max_length=250)
    imh= models.ImageField(upload_to='pics')
    dsc= models.TextField()
class team(models.Model):
    nme1= models.CharField(max_length=250)
    imh1= models.ImageField(upload_to='team_pic')
    dsc1= models.TextField()
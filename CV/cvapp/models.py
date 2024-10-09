from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='files')

class Cv(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    id_number = models.CharField(max_length=13)
    address = models.TextField()
    education = models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    skills = models.TextField()
    experience = models.TextField()

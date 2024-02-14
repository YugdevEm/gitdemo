from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name=models.CharField(max_length=18,verbose_name='enter your name : ')
    last_name=models.CharField(max_length=18)
    phone=models.BigIntegerField()
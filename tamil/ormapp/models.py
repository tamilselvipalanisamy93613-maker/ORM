from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
      car_Name=models.CharField(max_length=10)
      carID=models.IntegerField(primary_key=True)
      fuelTupe=models.CharField(max_length=10)
      color=models.CharField(max_length=6)
      brand=models.CharField(max_length=8)
class Car_DBAdmin(admin.ModelAdmin):
      list_display=["car_Name","carID","fuelTupe","color","brand"]

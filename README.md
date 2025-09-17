# Ex02 Django ORM Web Application
## Date: 17.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from.models import Car_DB,Car_DBAdmin
admin.site.register(Car_DB,Car_DBAdmin)
```


## OUTPUT
![alt text](<Screenshot (19).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully

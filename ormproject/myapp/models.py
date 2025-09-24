from django.db import models
from django.contrib import admin
class car_inventory(models.Model):
    car_brand=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    mileage=models.IntegerField()
    engine_type=models.CharField(max_length=20)
    manfg_date=models.DateField()
class car_admin(admin.ModelAdmin):
    list_display=('car_brand','car_model','mileage','engine_type','manfg_date')

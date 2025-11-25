from django.db import models
from django.contrib import admin
class car(models.Model):
    car_model=models.CharField(max_length=100)
    size=models.IntegerField()
    colour=models.CharField()
    price_range=models.IntegerField()
class carAdmin(admin.ModelAdmin):
    list_display=['car_model','size','colour','price_range']    


from django.db import models
from django.urls import reverse
# Create your models here.


class Daycare(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.IntegerField()
    discription = models.BooleanField(default=True)
    intro1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    intro2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    intro3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    intro4 = models.DateTimeField(auto_now_add=True)
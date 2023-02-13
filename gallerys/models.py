from django.db import models

# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=20)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name
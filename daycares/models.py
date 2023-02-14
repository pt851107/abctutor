from django.db import models
# Create your models here.


class Daycare(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discription = models.CharField(max_length=50)
    intro1 = models.CharField(max_length=50)
    intro2 = models.CharField(max_length=50)
    intro3 = models.CharField(max_length=50)
    intro4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Price(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discription = models.TextField(max_length=20)
    intro1 = models.CharField(max_length=20)
    intro2 = models.CharField(max_length=20)
    intro3 = models.CharField(max_length=20)
    intro4 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

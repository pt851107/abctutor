from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    self_intro = models.TextField(blank=True)
    qualification_1 = models.CharField(max_length=50)
    qualification_2 = models.CharField(max_length=50)
    qualification_3 = models.CharField(max_length=50)
    qualification_4 = models.CharField(max_length=50)
    qualification_5 = models.CharField(max_length=50)
    facebook = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name

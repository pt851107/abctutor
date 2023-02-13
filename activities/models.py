from django.db import models
from django.urls import reverse
# Create your models here.
    
class Activity(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    activity_date = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    payment_details = models.TextField(blank=True)
    enrollment_info = models.TextField(blank=True)
    safety_info = models.TextField(blank=True)
    terms_and_conditions = models.TextField(blank=True)
    fees = models.IntegerField()
    available = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'))
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('activities:activity_detail',
                       args=[self.id,self.slug])   
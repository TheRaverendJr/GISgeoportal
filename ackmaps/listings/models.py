from random import choices
from django.contrib.gis.db import models
from django.utils import timezone
#location imports
from django.contrib.gis.geos import Point



# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=150)
    choices_listing_type = (
        ('Cathedral', 'Cathedral'),
        ('Church', 'Church'),
        ('Office', 'Office')
    )
    listing_type = models.CharField(max_length=20, choices=choices_listing_type)
    choices_archdeaconry =(
        ('Mathews Cathedral Archdeaconry', 'Mathews Cathedral Archdeaconry'),
        ('Emmanuel Archdeaconry', 'Emmanuel Archdeaconry'),
    ) 
    archdeaconry = models.CharField(max_length=150, null=True, blank=True, choices=choices_archdeaconry)
    parish = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    
    choices_property_status = (
        ('Registered', 'Registered'),
        ('Unregistered', 'Unregistered'),
    )
    property_status = models.CharField(max_length=20, blank=True, null=True, choices=choices_property_status)
    
    date_posted = models.TimeField(default=timezone.now)

    #adding location field - geodjango
    location = models.PointField(blank=True, null=True, srid=4326)
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")

    def __str__(self):
        return self.title
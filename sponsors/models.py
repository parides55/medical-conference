from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Sponsor(models.Model):
    
    STATUS = (
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Other', 'Other'),
    )
    
    name = models.CharField(max_length=200)
    logo = CloudinaryField('image', default='placeholder')
    url = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS, default='Other')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.is_active}'
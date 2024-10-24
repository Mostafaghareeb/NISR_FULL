from django.db import models

# Create your models here.
class Order(models.Model):
    width = models.CharField(max_length=20)
    ratio = models.CharField(max_length=20)
    rim_size = models.CharField(max_length=20)
    speed_rating = models.CharField(max_length=20)
    governorate = models.CharField(max_length=20)
    delivery = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'order'
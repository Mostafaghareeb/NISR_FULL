from django.db import models

class Customize_your_tire(models.Model):
    logo = models.ImageField(upload_to='logos/')
    tire_color = models.CharField(max_length=20)
    trim = models.CharField(max_length=20)
    class Meta:
        verbose_name= 'design'

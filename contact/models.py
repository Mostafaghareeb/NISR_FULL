from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50)
    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name = 'message'    
    

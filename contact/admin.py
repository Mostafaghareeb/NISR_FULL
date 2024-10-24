from django.contrib import admin
from .models import Contact


class Admin(admin.ModelAdmin):
    search_fields = ['name']
    

admin.site.register(Contact, Admin)
admin.site.site_header = 'NISR administration'
admin.site.site_title = 'NISR.Tires'


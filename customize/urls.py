from django.urls import path
from . import views



urlpatterns = [
    path('Customize_tap/', views.Customize_tap, name='Customize_tap')
] 
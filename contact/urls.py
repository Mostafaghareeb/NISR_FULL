from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page2/', views.page2, name='page2'),
    path('offers_page/', views.offers_page, name='offers_page'),
    path('Customize_tap/', views.Customize_tap, name='Customize_tap'),
]
from django import forms
from .models import Customize_your_tire

class Customize_your_tireForm(forms.ModelForm):
    class Meta:
        model = Customize_your_tire
        fields = '__all__'
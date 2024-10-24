from django.shortcuts import render
from .models import Customize_your_tire
from .forms import Customize_your_tireForm
# Create your views here.
def Customize_tap(request):
    if request.method == 'POST':
        data = Customize_your_tireForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
    return render(request, 'html/Customize_tap.html')
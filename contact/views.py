from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.
 
def index(request):
    if request.method == 'POST':
        data = ContactForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'html/index.html')
    

def page2(request):
    return render(request, 'html/page2.html')

def offers_page(request):
    return render(request, 'html/offers_page.html')

def Customize_tap(request):
    return render(request, 'html/Customize_tap.html')

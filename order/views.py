from django.shortcuts import render
from .forms import OrderForm
def page2(request):
    if request.method == 'POST':
        data = OrderForm(request.POST)
        if data.is_valid():
            data.save()
            


    return render(request, 'html/page2.html')

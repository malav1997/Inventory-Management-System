from django.shortcuts import render, HttpResponse
import os
from django.shortcuts import render, redirect
from basic.models import Item, Stock
import datetime
import shutil
from .forms import SellForm


# Create your views here.
def sell(request):
    iserror=False
    items = Item.objects.all()
    form = SellForm(request.POST)
    my_list = {}
    if request.method == 'POST':
        if form.is_valid():
            item = request.POST['item']
            quantity = request.POST['quantity']
            stock = Stock.objects.filter(item=item).values('quantity')
            if int(quantity) <= stock[0].get('quantity'):
                iserror=False
                obj, created = Stock.objects.get_or_create(master=request.POST['master'], item=request.POST['item'])
                obj.quantity = obj.quantity - int(request.POST['quantity'])
                obj.save()
                
                #return render(request, 'sell/sell.html', {'go': my_list, 'form': form, 'iserror': iserror})

            else:
                iserror=True
    my_list = []
    for file in os.listdir("buy/static/pdf/"):
        if file.endswith(".pdf"):
            file = file[:len(file)-4]
            my_list.append(file)            
    return render(request, 'sell/sell.html', {'go': my_list, 'form': form, 'iserror': iserror})
    
def open_pdf(request, slug):
    with open('buy/static/pdf/'+slug+'.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+slug+'.pdf'
    return response

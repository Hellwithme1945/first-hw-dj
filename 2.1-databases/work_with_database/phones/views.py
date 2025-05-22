from django.shortcuts import render, get_object_or_404
from .models import Phone

def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    return render(request, 'product.html', {'phone': phone})
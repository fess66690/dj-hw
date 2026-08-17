from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort', 'name')

    if sort_by == 'name':
        order_by = 'name'
    elif sort_by == 'min_price':
        order_by = 'price'
    elif sort_by == 'max_price':
        order_by = '-price'
    else:
        order_by = 'name'

    phones = Phone.objects.all().order_by(order_by)

    template = 'catalog.html'

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404 (Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)

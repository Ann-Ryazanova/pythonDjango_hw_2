from django.shortcuts import render
from django.views.generic import DetailView

from catalog.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


def home(request):
    product_list = Product.objects.all()

    context = {
        'object_list': product_list,
        'title': 'Продуктовая лавка'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Имя: {name}, телефон: {phone};\n'
              f'Сообщение: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def product_card(request, pk):

    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': 'Страница продукта'
    }

    return render(request, 'catalog/product.html', context)

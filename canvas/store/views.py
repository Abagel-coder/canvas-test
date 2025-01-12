from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })
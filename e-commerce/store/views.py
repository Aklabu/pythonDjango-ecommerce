from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    products_by_category = {cat: Product.objects.filter(category=cat) for cat in categories}
    return render(request, 'store/home.html', {'products_by_category': products_by_category})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all_products.html', {'products': products})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recommendations = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'recommendations': recommendations
    })

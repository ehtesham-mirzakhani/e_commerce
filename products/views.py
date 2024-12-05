from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from products.models import Product


# Create your views here.

# class ProductListView(View):
#     def get(self, request):
#         products = Product.objects.all()

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'product'
    paginate_by = 1

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'

from django.db.models import Count
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from products.models import Product, ProductCategory, ProductBrand


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'product'
    paginate_by = 1
    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('cate')
        brand_name = self.kwargs.get('brand')
        if brand_name is not None:
            query = Product.objects.filter(brand__url_title__iexact=brand_name)
        if category_name is not None:
            query = Product.objects.filter(category__url_title__iexact=category_name)
        return query
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'

def product_categories_component(request):
    Product_categories = ProductCategory.objects.filter(is_active=True,is_delete=False)
    context = {
        'categories': Product_categories,
    }
    return  render(request,'products/components/product_categories_component.html',context)

def product_brands_component(request):
    Product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context ={
        'brands': Product_brands,
    }
    return render(request, 'products/components/product_brands_component.html',context)
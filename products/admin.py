from django.contrib import admin

from products.models import Product, ProductCategory,ProductTag,ProductBrand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','is_active','is_delete')
    list_filter = ('is_active','category')
    prepopulated_fields = {'slug': ('title',)}
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','url_title')
@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
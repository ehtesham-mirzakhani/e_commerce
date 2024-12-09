from django.contrib import admin
from  . import  models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('is_paid', )
@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('final_price', )
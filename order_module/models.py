from django.db import models
from account_module.models import User
from products.models import Product
from django.core.validators import MinValueValidator

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده',default=False)
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'
    def calculate_total_price(self):
        total_amount = 0
        order_details = self.orderdetail_set.prefetch_related('product').all()  # بهینه‌سازی با prefetch_related
        for order_detail in order_details:
            price = order_detail.final_price if self.is_paid else order_detail.product.price
            total_amount += price * order_detail.count
        # return total_amount
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد',validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
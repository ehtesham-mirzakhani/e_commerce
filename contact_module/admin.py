from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
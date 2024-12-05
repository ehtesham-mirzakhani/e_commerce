from django.contrib import admin
from . import models
@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'address')

@admin.register(models.FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(models.FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active','url')
    list_editable = ( 'is_active', 'url' )
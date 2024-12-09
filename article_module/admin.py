from django.contrib import admin
from . import models

@admin.register(models.ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title','parent','is_active' )
    list_editable = ['is_active','url_title','parent']

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','slug','author')
    list_editable = ['is_active',]
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
@admin.register(models.ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('user','create_date')
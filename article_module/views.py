from django.views.generic import DetailView
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali

from django.shortcuts import render

from article_module.models import Article, ArticleCategory, ArticleComment


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/article_page.html'
    context_object_name = 'articles'
    paginate_by = 5
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = kwargs.get('object')
        context['comments']=(ArticleComment.objects.filter(article_id=article.id,parent = None).order_by('-create_date')
                             .prefetch_related('articlecomment_set'))
        return context
def article_categories_component(request):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True,parent=None)
    context = {'main_categories':article_main_categories}
    return render(request,'article_module/components/article_categories_components.html',context)
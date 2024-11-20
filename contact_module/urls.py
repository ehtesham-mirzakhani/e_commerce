from django.urls import path
from contact_module import views
urlpatterns = [
    path('',views.contact_us_page , name='contact_us_page'),
]
from django.urls import path
from contact_module import views
urlpatterns = [
    path('',views.ContactUsView.as_view() , name='contact_us_page'),
]
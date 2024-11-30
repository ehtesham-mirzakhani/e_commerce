from django.urls import path

from . import views

urlpatterns = [
    path('', views.registerView.as_view(), name='register_page'),
    path('activate-account/<active_code>',views.ActivateAccountView.as_view(),name='activate_account'),
    path('login', views.LoginView.as_view(), name='login_page'),
]
from datetime import datetime, timedelta

from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from account_module.forms import RegistrationForm, LoginForm,ForgotPasswordForm,ResetPasswordForm
from account_module.models import User
from django.utils.crypto import get_random_string
from utils.email_service import send_email

class registerView(View):
    def get(self, request):
        register_form = RegistrationForm()
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html',context)
    def post(self, request):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            is_username = User.objects.filter(username=username).exists()
            user_email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            is_email = User.objects.filter(email__iexact=user_email).exists()
            user_phone = register_form.cleaned_data.get('phone')
            is_phone = User.objects.filter(phone__iexact=user_phone).exists()
            if is_email:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            elif is_phone:
                register_form.add_error('phone', 'تلفن وارد شده تکراری است')
            elif is_username:
                register_form.add_error('username', 'نام کاربری تکراری است')
            else:
                new_user = User.objects.create_user(
                    username=register_form.cleaned_data.get('username'),
                    email=user_email,
                    phone=user_phone,
                    active_code = get_random_string(72),
                    is_active=False,
                )
                new_user.set_password(password)
                request.session['user_id']= new_user.id
                new_user.save()
                send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user},
                           'emails/activate_account.html')
                return redirect(reverse('register_page'))
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)

class ActivateAccountView(View):
    def get(self, request, active_code):

        user = User.objects.filter(active_code__iexact=active_code).first()
        is_expire= user.is_expire()
        if user is not None:
            if not is_expire:
                if not user.is_active:
                    user.is_active = True
                    user.active_code = get_random_string(75)
                    user.save()
                    print('your account is active')
                    return redirect(reverse('login_page'))
                else:
                    print('your account is already active')
                    return redirect(reverse('register_page'))
            else:
                print('your active code is expired ')
                user.active_code = get_random_string(75)
                user.expire_date = datetime.now() + timedelta(minutes=1)
                user.save()
                send_email(
                    'فعال سازی حساب کاربری - کد جدید',
                    user.email,
                    {'user': user},
                    'emails/activate_account.html'
                )
                return redirect(reverse('login_page'))
        raise Http404

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما اکتیو نشده است')
                else:
                    is_password_correct = user.check_password(login_form.cleaned_data.get('password'))
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کاربر یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات مورد نظر یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request,'account_module/forgot_password.html',context)
    def post(self, request):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('تغییر کلمه عبور', user.email, {'user': user},
                           'emails/forgot_password.html')
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)

class ResetPasswordView(View):
    def get(self, request,active_code):
        user = User.objects.filter(active_code__iexact=active_code).first()
        if user is None:
            return redirect('login_page')
        reset_pass_form = ResetPasswordForm()
        context = {'reset_pass_form':reset_pass_form,'user':user}
        return render(request,'account_module/reset_password.html',context)
    def post(self,request,active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user = User.objects.filter(active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect('login_page')
            user.set_password(reset_pass_form.cleaned_data.get('password'))
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect('login_page')
        context = {'reset_pass_form':reset_pass_form,'user':user}
        return render(request,'account_module/reset_password.html',context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from random import randint
from .forms import RegisterForm, LoginForm, CheckOtpForm
from .models import Otp

User = get_user_model()


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send sms here
            receptor = cd['phone']
            rand_code = randint(1000, 9999)
            print(rand_code)
            # end
            Otp.objects.create(phone=cd['phone'], code=rand_code)

            messages.success(request, 'Code Sent To Your Phone.')
            return redirect(reverse('accounts:check_otp') + f'?phone={receptor}')


class CheckTopView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'accounts/check_otp.html', {'form': form})

    def post(self, request):
        form = CheckOtpForm(request.POST)
        phone = request.GET.get('phone')
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(phone=phone, code=cd['code']).exists():
                user = User.objects.create(phone=phone)
                # login(request, user)
                messages.success(request, 'Register Was Successful.')
                return redirect('shop:index')
        else:
            messages.warning(request, 'Something Went Wrong.')
            return redirect(request.META.get('HTTP_REFERER'))


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully.')
                return redirect(request.META.get('HTTP_REFERER'))

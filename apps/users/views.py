from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from apps.users.forms import LoginForm, RegisterForm


class UserRegisterView():
    pass
class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                messages.success(request, "user succesfully loged in")
                return redirect("home")
            else:
                messages.warning(request, "User not found")
                return redirect("users:login")
        else:
            return render(request, "user/login.html", {"form": form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,'user/logout.html')
    def post(self, request):
        messages.info(request, f"{request.user.username} user successfulley loged out")
        logout(request)
        return redirect("users:login")


class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "user/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully registered")
            return redirect('users:login')
        else:
            return render(request, "user/register.html", {"form": form})

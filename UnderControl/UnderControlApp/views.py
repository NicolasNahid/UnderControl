
from django.shortcuts import redirect, render
from UnderControlApp.forms import  UserRegisterForm, UpdateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordChangeView
# from django.contrib.messages.views import SuccessMessageMixin
# from django.views.defaults import page_not_found


def inicio(request):

    return render(request, 'UnderControlApp/index.html')

def app(request):

    return render(request, 'UnderControlApp/app.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("app")
            else:
               return redirect("login")
        else:
            return redirect("login")

    form = AuthenticationForm()

    return render(request, 'UnderControlApp/login.html', {'form': form})


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        return render(request, "UnderControlApp/register.html", {"form":form})

    form = UserRegisterForm()

    return render(request, 'UnderControlApp/register.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect("inicio")
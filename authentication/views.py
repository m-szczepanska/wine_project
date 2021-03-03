from django.contrib.auth import login as login_method
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from authentication.forms import LoginForm


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    elif request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = get_object_or_404(User, email=email)

        if user.check_password(password):
            login_method(request, user)
            return redirect('wines:wines_list')

        else:
            return redirect('authentication:login')



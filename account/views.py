from django.contrib.auth import login as auth_signin

# from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
# from django.contrib.auth.models import User
# from django.urls import reverse
# from .models import CustomUser
from .forms import SignUpForm
from .forms import SignInForm


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


class IndexView(TemplateView):
    template_name = 'account/index.html'


index = IndexView.as_view()


class SignIn(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': SignInForm(),
        }
        return render(request, 'account/index.html', context)

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/index.html', {'form': form})

        return render(request, 'account/main.html', {'form': form})

        auth_signin(request, form)
        # custom_user = request.custom_user
        # auth_signin(request, CustomUser.pk)

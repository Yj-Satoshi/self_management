from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import View
# Create your views here.


def signup(request):
    form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

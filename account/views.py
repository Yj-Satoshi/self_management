from django.contrib.auth import login as auth_signin
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.views.generic import TemplateView
from django.views import View


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
        return render(request, 'account/signin.html', context)

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/index.html', {'form': form})

        return render(request, 'account/signin.html', {'form': form})

        auth_signin(request, form)


def users_detail(request, pk):
    user = request.user
    return render(request, 'account/main.html', {'user': user})

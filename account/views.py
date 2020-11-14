from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import login as auth_signin
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.views.generic import TemplateView
from django.views import View
# from django.views.generic import (
#     ListView
# )

from monthly_goal.models import MonthlyGoal
# from monthly_goal.views import OnlyYouMixin


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


class MyPageView(UserPassesTestMixin):
    def users_detail(request, user_id):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(custom_user_id_id=user_id)
        return render(
            request, 'account/main.html', {'user': user, 'monthly_goals': monthly_goals})
        # monthly_goal_list = MonthlyGoal.objects.filter(custom_user_id=user_id)
    # return render(request, 'account/main.html', {"monthly_goals": monthly_goal_list})

    # model = MonthlyGoal
    # template_name = 'account/main.html'
    # context_object_name = 'manthly_goals'
    # ordering = ['-date_posted']

# class MonthlyGoalListView(OnlyYouMixin, ListView):
#     model = MonthlyGoal
#     template_name = 'account/.html'
#     context_object_name = 'monthly_goals'
#     ordering = ['-date_posted']

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import WeeklyAction
from monthly_goal.models import MonthlyGoal
from monthly_goal.views import OnlyYouMixin
from account.views import MyPageView
from django.shortcuts import get_object_or_404


class WeeklyActionDetailView(DetailView, OnlyYouMixin,  LoginRequiredMixin):
    model = WeeklyAction


class WeeklyActionCreateView(CreateView, MyPageView, MonthlyGoal):
    model = WeeklyAction
    fields = [
        'week_no', 'goal_action', 'why_need_goal'
        ]
    # success_url = '/signin'

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        weekly_action = form.save(commit=False)
        monthly_goal_pk = self.kwargs['monthly_goal_id']
        weekly_action.monthly_goal = get_object_or_404(MonthlyGoal, pk=monthly_goal_pk)
        weekly_action.save()
        return super().form_valid(form)
        return redirect('account:main', pk=self.request.user.id)


class WeeklyActionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = WeeklyAction
    fields = [
        'year', 'month', 'category', 'score', 'revised_goal', 'why_revise'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            return True
        return False

    success_url = '/signin'


class WeeklyActionDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = WeeklyAction
    success_url = '/signin'

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            return True
        return False

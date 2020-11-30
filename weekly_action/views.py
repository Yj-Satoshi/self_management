from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monthly_goal'] = MonthlyGoal.objects.get(id=self.object.monthly_goal_id)
        return context


class WeeklyActionCreateView(CreateView, MyPageView, MonthlyGoal):
    model = WeeklyAction
    fields = [
        'week_no', 'goal_action', 'why_select_action'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        weekly_action = form.save(commit=False)
        monthly_goal_pk = self.kwargs['monthly_goal_id']
        weekly_action.monthly_goal = get_object_or_404(MonthlyGoal, pk=monthly_goal_pk)
        weekly_action.save()
        return super().form_valid(form)

    success_url = '/main'


class WeeklyActionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = WeeklyAction
    fields = [
        'score', 'after_memo', 'week_no', 'goal_action', 'why_select_action'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            return True
        return False

    success_url = '/main'


class WeeklyActionDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = WeeklyAction

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            return True
        return False

    success_url = '/main'
    # def get_success_url(self):
    #     return reverse('account:main', kwargs={'user_id': self.kwargs['pk']})

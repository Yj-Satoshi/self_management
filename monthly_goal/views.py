from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import MonthlyGoal
from account.views import MyPageView


class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class MonthlyGoalDetailView(DetailView, OnlyYouMixin,  LoginRequiredMixin):
    model = MonthlyGoal


class MonthlyGoalCreateView(CreateView, MyPageView):
    model = MonthlyGoal
    fields = [
        'year', 'month', 'category', 'goal', 'why_need_goal'
        ]
    success_url = '/signin'

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)


class MonthlyGoalUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = MonthlyGoal
    fields = [
        'year', 'month', 'category', 'sccore', 'revised_goal', 'why_revise'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            return True
        return False

    success_url = '/signin'


class MonthlyGoalDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = MonthlyGoal
    success_url = '/signin'

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            return True
        return False

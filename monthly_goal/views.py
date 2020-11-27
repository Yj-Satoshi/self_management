from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import MonthlyGoal
from weekly_action.models import WeeklyAction
from account.views import MyPageView


class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class MonthlyGoalDetailView(DetailView, OnlyYouMixin,  LoginRequiredMixin):
    model = MonthlyGoal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weekly_action'] = WeeklyAction.objects.filter(monthly_goal_id=self.object.id)
        return context


class MonthlyGoalCreateView(CreateView, MyPageView):
    model = MonthlyGoal
    fields = [
        'year', 'month', 'category', 'goal', 'why_need_goal'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        user = self.request.user
        return reverse('account:main', kwargs={'user_id': user.id})


class MonthlyGoalUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = MonthlyGoal
    fields = [
        'score', 'after_memo', 'year', 'month', 'category',  'revised_goal', 'why_revise'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            return True
        return False

    def get_success_url(self):
        user = self.request.user
        return reverse('account:main', kwargs={'user_id': user.id})


class MonthlyGoalDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = MonthlyGoal

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            return True
        return False

    def get_success_url(self):
        user = self.request.user
        return reverse('account:main', kwargs={'user_id': user.id})

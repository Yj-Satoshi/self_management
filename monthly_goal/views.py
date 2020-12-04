from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import MonthlyGoal
from weekly_action.models import WeeklyAction


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


class MonthlyGoalCreateView(CreateView):
    model = MonthlyGoal
    fields = [
        'year', 'month', 'category', 'goal', 'why_need_goal'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        messages.info(self.request, "目標作成しました。次はアクションを作成下さい")
        return super().form_valid(form)

    success_url = '/main'


class MonthlyGoalUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = MonthlyGoal
    fields = [
        'score', 'after_memo', 'year', 'month', 'category',  'revised_goal', 'why_revise'
        ]

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        messages.info(self.request, "目標を更新しました。")
        return super().form_valid(form)

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            return True
        return False

    success_url = '/main'


class MonthlyGoalDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = MonthlyGoal

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.custom_user:
            messages.info(self.request, "目標を削除しました。")
            return True
        return False

    success_url = '/main'

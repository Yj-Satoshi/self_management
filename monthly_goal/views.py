from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
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


class MonthlyGoalListView(OnlyYouMixin, ListView):
    model = MonthlyGoal
#   template_name = 'blog/home.html'
#   context_object_name = 'posts'
#   ordering = ['-date_posted']


class MonthlyGoalDetailView(OnlyYouMixin, DetailView):
    model = MonthlyGoal


class MonthlyGoalCreateView(OnlyYouMixin, LoginRequiredMixin, CreateView, MyPageView):
    model = MonthlyGoal
    fields = [
        'year', 'month', 'category', 'goal', 'why_need_goal', 'custom_user_id'
        ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MonthlyGoalUpdateView(OnlyYouMixin, LoginRequiredMixin, UpdateView):
    model = MonthlyGoal
    # fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.author:
            return True
        return False


class MonthlyGoalDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = MonthlyGoal
    # success_url = '/'

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.author:
            return True
        return False

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
# from account.models import CustomUser
from .models import MonthlyGoal


class MonthlyGoalListView(ListView):
    model = MonthlyGoal
#   template_name = 'blog/home.html'
#   context_object_name = 'posts'
#   ordering = ['-date_posted']


class MonthlyGoalDetailView(DetailView):
    model = MonthlyGoal


class MonthlyGoalCreateView(LoginRequiredMixin, CreateView):
    model = MonthlyGoal
    fields = [
        'month', 'category', 'goal', 'why_need_goal', 'category', 'category'
        ]
    # user = request.user

    # def post_detail(request, pk):

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MonthlyGoalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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


class MonthlyGoalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MonthlyGoal
    success_url = '/'

    def test_func(self):
        monthly_goal = self.get_object()
        if self.request.user == monthly_goal.author:
            return True
        return False

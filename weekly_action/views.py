from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import WeeklyAction
from monthly_goal.models import MonthlyGoal
from monthly_goal.views import OnlyYouMixin


class WeeklyActionDetailView(DetailView, OnlyYouMixin,  LoginRequiredMixin):
    model = WeeklyAction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monthly_goal'] = MonthlyGoal.objects.get(id=self.object.monthly_goal_id)
        return context


class WeeklyActionCreateView(CreateView, MonthlyGoal):
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
        messages.info(self.request, 'アクション作成しました。作成したアクションを実施下さい（P "D" CA）')
        return super().form_valid(form)

    success_url = '/main'


class WeeklyActionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = WeeklyAction
    fields = [
        'score', 'after_memo', 'week_no', 'goal_action', 'why_select_action'
        ]
    success_url = '/main'

    def form_valid(self, form, request):
        form.instance.custom_user = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.POST['score']:
            messages.info(request, "アクションを修正しました。")
        elif request.POST['score'] == "1":
            messages.info(request, "アクションを評価しました。反省点を無駄にせず、今後のアクションに生かしましょう")
        elif request.POST['score'] == "5":
            messages.info(request, "アクションを評価しました。その調子で頑張りましょう")
        else:
            messages.info(request, "アクションを評価しました。次のアクションも頑張りましょう")
        return redirect('/main')

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            return True
        return False


class WeeklyActionDeleteView(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    model = WeeklyAction

    def test_func(self):
        weekly_action = self.get_object()
        if self.request.user == weekly_action.custom_user:
            messages.info(self.request, "アクションを削除しました。")
            return True
        return False

    success_url = '/main'

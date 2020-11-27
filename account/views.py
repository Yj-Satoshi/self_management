from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
# from monthly_goal.forms import GoalScoreForm
# from weekly_action.forms import ActionScoreForm
from django.views.generic import TemplateView
from django.views import View
from monthly_goal.models import MonthlyGoal
from weekly_action.models import WeeklyAction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .mixins import MonthCalendarMixin, WeekCalendarMixin
import datetime
import math
date_string = datetime.datetime.now()

if date_string.day % 7 == 2:
    if date_string.strftime('%a') == 'Mon' or 'Sun':
        add = +1
    elif date_string.strftime('%a') == 'Tue':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 3:
    if date_string.strftime('%a') == 'Tue' or 'Mon':
        add = +1
    elif date_string.strftime('%a') == 'Wed':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 4:
    if date_string.strftime('%a') == 'Wed' or 'Tue':
        add = +1
    elif date_string.strftime('%a') == 'Thu':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 5:
    if date_string.strftime('%a') == 'Thu' or 'Wed':
        add = +1
    elif date_string.strftime('%a') == 'Fri':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 6:
    if date_string.strftime('%a') == 'Fri' or 'Thu':
        add = +1
    elif date_string.strftime('%a') == 'Sat':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 0:
    if date_string.strftime('%a') == 'Sat' or 'Fri':
        add = +1
    elif date_string.strftime('%a') == 'Sun':
        add = -1
    else:
        add = 0
elif date_string.day % 7 == 1:
    if date_string.strftime('%a') == 'Sun' or 'Sat':
        add = +1
    elif date_string.strftime('%a') == 'Mon':
        add = -1
    else:
        add = 0
this_week = math.ceil(date_string.day / 7) + add


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


class MyPageView(MonthCalendarMixin, WeekCalendarMixin, UserPassesTestMixin, LoginRequiredMixin):
    # マイページに自己評価入力フォーム導入予定
    # def post_goal_score(request):
    #     if request.method == 'POST':
    #         goal_score = GoalScoreForm(request.POST)
    #     else:
    #         goal_score = GoalScoreForm()
    #     return goal_score

    # def post_action_score(request):
    #     if request.method == 'POST':
    #         action_score = ActionScoreForm(request.POST)
    #     else:
    #         action_score = ActionScoreForm()
    #     return action_score

    def paginate_queryset(request, queryset, count):
        paginator = Paginator(queryset, count)
        page = request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return page_obj

    def get_context_month_data(self):
        month_calendar_context = self.get_month_calendar()
        return month_calendar_context

    def get_context_week_data(self):
        week_calendar_context = self.get_week_calendar()
        return week_calendar_context

    def users_detail(request, user_id):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id).exclude(score__isnull=False).order_by('year', 'month', 'goal')

        weekly_actions = WeeklyAction.objects.filter(
                    custom_user_id=user.id).order_by('score', 'week_no', 'goal_action')[:100]
        this_monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id, year=date_string.year, month=date_string.month
            ).exclude(score__isnull=False).order_by('year', 'month', 'goal')
        this_weekly_actions = WeeklyAction.objects.filter(
                    custom_user_id=user.id, week_no=this_week
                    ).exclude(score__isnull=False).order_by('goal_action')[:10]
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 5)

        month_calendar_context = MyPageView().get_context_month_data
        week_calendar_context = MyPageView().get_context_week_data

        # goal_score = MyPageView.post_goal_score(request)
        # action_score = MyPageView.post_action_score(request)

        context = {
            'user': user,
            'monthly_goals': page_obj.object_list,
            'weekly_actions': weekly_actions,
            'this_weekly_actions': this_weekly_actions,
            'this_monthly_goals': this_monthly_goals,
            'page_obj': page_obj,
            'month_calendar_context': month_calendar_context,
            'week_calendar_context': week_calendar_context,
            'this_week': this_week,
            # 'goal_score_form': goal_score,
            # 'action_score_form': action_score,
        }
        return render(
            request, 'account/main.html', context)


class MyPageScoredView(MyPageView):
    def scored_users_detail(request, user_id):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id, score__isnull=False).order_by('-year', '-month', 'goal')
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 5)
        context = {
            'user': user,
            'monthly_goals': page_obj.object_list,
            'page_obj': page_obj,
        }
        return render(
            request, 'account/main_scored.html', context)

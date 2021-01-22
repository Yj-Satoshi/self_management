from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from .models import CustomUser
from monthly_goal.models import MonthlyGoal
from weekly_action.models import WeeklyAction
from .forms import SignUpForm, UserUpdateForm  # SignInForm
from .mixins import MonthCalendarMixin, WeekCalendarMixin
import datetime
import math
import matplotlib
import matplotlib.pyplot as plt
from django.db.models import Avg
import io
from django.http import HttpResponse
matplotlib.use('Agg')
date_string = datetime.datetime.now()

add = 0
if date_string.strftime('%a') == 'Mon':
    if date_string.day % 7 != 1:
        add = +1
elif date_string.strftime('%a') == 'Tue':
    if date_string.day % 7 > 2 or date_string.day % 7 == 0:
        add = +1
elif date_string.strftime('%a') == 'Wed':
    if date_string.day % 7 > 3 or date_string.day % 7 == 0:
        add = +1
elif date_string.strftime('%a') == 'Thu':
    if date_string.day % 7 > 4 or date_string.day % 7 == 0:
        add = +1
elif date_string.strftime('%a') == 'Fri':
    if date_string.day % 7 > 5 or date_string.day % 7 == 0:
        add = +1
elif date_string.strftime('%a') == 'Sat':
    if date_string.day % 7 == 0:
        add = +1
this_week = math.ceil(date_string.day / 7) + add


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "アカウント作成しました。")
            return redirect('/')
        else:
            form = SignUpForm()
            messages.error(request, "アカウント作成に失敗しました。もう一度入力下さい。")
    return render(request, 'account/signup.html', {'form': form})


class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'account/index.html'
    success_url = '/main'
    success_message = "サインインしました。"


class UserUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'account/user_update.html'

    def form_valid(self, form):
        form.instance.custom_user = self.request.user
        messages.info(self.request, "プロフィールを更新しました。")
        return super().form_valid(form)
    success_url = '/main'


class MyPageView(MonthCalendarMixin, WeekCalendarMixin, UserPassesTestMixin, LoginRequiredMixin):

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

    def users_detail(request):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id).exclude(score__isnull=False).order_by('year', 'month', 'goal')

        weekly_actions = WeeklyAction.objects.filter(
                    custom_user_id=user.id).order_by('score', 'week_no', 'goal_action')
        this_monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id, year=date_string.year, month=date_string.month
            ).exclude(score__isnull=False).order_by('year', 'month', 'goal')
        this_weekly_actions = WeeklyAction.objects.filter(
                    custom_user_id=user.id, week_no=this_week
                    ).exclude(score__isnull=False).order_by('goal_action')
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 5)

        month_calendar_context = MyPageView().get_context_month_data
        week_calendar_context = MyPageView().get_context_week_data
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
        }
        return render(
            request, 'account/main.html', context)


class MyPageScoredView(MyPageView):
    def scored_users_detail(request):
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


class MonthScoreChart():
    # def month_count(n):
    #     if date_string.month - n <= 0:
    #         month = date_string.month - n + 12
    #         return month

    # def year_count(n):
    #     if date_string.month - n <= 0:
    #         year = date_string.year - 1
    #         return year

    def setPlt(request):
        user = request.user
        month1 = date_string.month
        month2 = date_string.month - 1
        month3 = date_string.month - 2
        month4 = date_string.month - 3
        month5 = date_string.month - 4
        month6 = date_string.month - 5

        year1 = date_string.year
        year2 = date_string.year
        year3 = date_string.year
        year4 = date_string.year
        year5 = date_string.year
        year6 = date_string.year

        if date_string.month - 1 <= 0:
            month2 = date_string.year + 11
            year2 = date_string.year - 1
        elif date_string.month - 2 <= 0:
            month3 = date_string.year + 10
            year3 = date_string.year - 1
        elif date_string.month - 3 <= 0:
            month4 = date_string.year + 9
            year4 = date_string.year - 1
        elif date_string.month - 4 <= 0:
            month5 = date_string.year + 8
            year5 = date_string.year - 1
        elif date_string.month - 4 <= 0:
            month6 = date_string.year + 7
            year6 = date_string.year - 1

        month1_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year1, month=month1
                ).exclude(score__isnull=False).aggregate(Avg('score'))

        month2_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year2,
                    month=month2
                    ).exclude(score__isnull=False).aggregate(Avg('score'))

        month3_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year3,
                    month=month3
                    ).exclude(score__isnull=False).aggregate(Avg('score'))

        month4_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year4,
                    month=month4
                    ).exclude(score__isnull=False).aggregate(Avg('score'))

        month5_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year5,
                    month=month5
                    ).exclude(score__isnull=False).aggregate(Avg('score'))

        month6_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year6,
                    month=month6
                    ).exclude(score__isnull=False).aggregate(Avg('score'))

        y = [
            month6_goals_score_ave,
            month5_goals_score_ave,
            month4_goals_score_ave,
            month3_goals_score_ave,
            month2_goals_score_ave,
            month1_goals_score_ave
            ]
        x = [
            month1,
            month2,
            month3,
            month4,
            month5,
            month6
            ]
        plt.plot(x, y, color='#00d5ff')
        plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
        plt.xlabel("月")
        plt.ylabel("目標評価平均")

    # def setPlt(request):
    #     x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    #     y = [3, 5, 0, 5, 6, 10, 2]
    #     plt.plot(x, y, color='#00d5ff')
    #     plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    #     plt.xlabel("Date")
    #     plt.ylabel("km")

    def plt2svg():
        buf = io.BytesIO()
        plt.savefig(buf, format='svg', bbox_inches='tight')
        s = buf.getvalue()
        buf.close()
        return s

    def get_svg(request):
        MonthScoreChart.setPlt(request)
        svg = MonthScoreChart.plt2svg()
        plt.cla()
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response

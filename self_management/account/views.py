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
import numpy as np
import pandas
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


class MonthScoreChart():

    def setPlt(request):
        user = request.user
        month1 = date_string.month - 1
        month2 = date_string.month - 2
        month3 = date_string.month - 3
        month4 = date_string.month - 4
        month5 = date_string.month - 5
        month6 = date_string.month - 6

        year1 = date_string.year
        year2 = date_string.year
        year3 = date_string.year
        year4 = date_string.year
        year5 = date_string.year
        year6 = date_string.year

        if date_string.month - 1 <= 0:
            month1 = date_string.month + 11
            year1 = date_string.year - 1
        if date_string.month - 2 <= 0:
            month2 = date_string.month + 10
            year2 = date_string.year - 1
        if date_string.month - 3 <= 0:
            month3 = date_string.month + 9
            year3 = date_string.year - 1
        if date_string.month - 4 <= 0:
            month4 = date_string.month + 8
            year4 = date_string.year - 1
        if date_string.month - 5 <= 0:
            month5 = date_string.month + 7
            year5 = date_string.year - 1
        if date_string.month - 6 <= 0:
            month6 = date_string.month + 6
            year6 = date_string.year - 1

        month1_6_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year6, month=month6, score__isnull=False
                )

        month1_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year1, month=month1, score__isnull=False
                )

        month2_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year2, month=month2, score__isnull=False
                )

        month3_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year3, month=month3, score__isnull=False
                )

        month4_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year4, month=month4, score__isnull=False
                )

        month5_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year5, month=month5, score__isnull=False
                )

        month6_goals_score_ave = MonthlyGoal.objects.select_related('score').filter(
                custom_user_id=user.id, year=year6, month=month6, score__isnull=False
                )

        y = np.array([
            month6_goals_score_ave.aggregate(Avg('score'))['score__avg'],
            month5_goals_score_ave.aggregate(Avg('score'))['score__avg'],
            month4_goals_score_ave.aggregate(Avg('score'))['score__avg'],
            month3_goals_score_ave.aggregate(Avg('score'))['score__avg'],
            month2_goals_score_ave.aggregate(Avg('score'))['score__avg'],
            month1_goals_score_ave.aggregate(Avg('score'))['score__avg']
            ])

        x = [
            str(year6) + "-" + str(month6),
            str(year5) + "-" + str(month5),
            str(year4) + "-" + str(month4),
            str(year3) + "-" + str(month3),
            str(year2) + "-" + str(month2),
            str(year1) + "-" + str(month1),
            ]

        y_1 = [0 for i in y if i is None]
        # x_1 = [x[int(i-1)] for i in y if i is not None]

        plt.plot(x, y_1, color='#808080')
        plt.scatter(x, y_1, color='#228B22')
        plt.title(r"$\bf{Score-average}$", color='blue')
        plt.xlabel("month")
        plt.ylabel("score")
        plt.ylim(0, 5)
        plt.xlim(0.5, 6.5)

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


class MyPageScoredView(MyPageView, MonthScoreChart):
    def scored_users_detail(request):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id, score__isnull=False).order_by('-year', '-month', 'goal')
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 5)

        month2 = date_string.month + 11
        year2 = date_string.year - 1
        month2_goals_score_ave = MonthlyGoal.objects.filter(
                    custom_user_id=user.id, year=year2,
                    month=month2, score__isnull=False
                    ).aggregate(Avg('score'))

        context = {
            'user': user,
            'monthly_goals': page_obj.object_list,
            'page_obj': page_obj,
            'score_ave': month2_goals_score_ave['score__avg'],
        }
        return render(
            request, 'account/main_scored.html', context)

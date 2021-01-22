import matplotlib
import matplotlib.pyplot as plt
from monthly_goal.models import MonthlyGoal
from django.db.models import Avg
import datetime
import io
from django.http import HttpResponse
matplotlib.use('Agg')
date_string = datetime.datetime.now()


class month_score_chart:
    def month_count(n):
        if date_string.month - n <= 0:
            month = date_string.month - n + 12
            return month

    def year_count(n):
        if date_string.month - n <= 0:
            year = date_string.year - 1
            return year

    user = request.user
    month1_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=date_string.year, month=date_string.month
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    month2_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year_count(1), month=month_count(1)
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    month3_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year_count(2), month=month_count(2)
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    month4_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year_count(3), month=month_count(3)
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    month5_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year_count(4), month=month_count(4)
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    month6_goals_score_ave = MonthlyGoal.objects.filter(
                custom_user_id=user.id, year=year_count(5), month=month_count(5)
                ).exclude(score__isnull=False).aggregate(Avg('score'))

    def plt2svg():
        buf = io.BytesIO()
        plt.savefig(buf, format='svg', bbox_inches='tight')
        s = buf.getvalue()
        buf.close()
        return s


    def setPlt(month6_goals_score_ave, month5_goals_score_ave, month4_goals_score_ave, month3_goals_score_ave, month2_goals_score_ave, month1_goals_score_ave):
        y = [
            month6_goals_score_ave, month5_goals_score_ave, month4_goals_score_ave,
            month3_goals_score_ave, month2_goals_score_ave, month1_goals_score_ave
            ]
        x = [
            month_score_chart.month_count(5),
            month_score_chart.month_count(4),
            month_score_chart.month_count(3),
            month_score_chart.month_count(2),
            month_score_chart.month_count(1),
            month_score_chart.month_count(0)
            ]
        plt.plot(x, y, color='#00d5ff')
        plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
        plt.xlabel("月")
        plt.ylabel("目標評価平均")

    def get_svg(request, month6_goals_score_ave, month5_goals_score_ave, month4_goals_score_ave, month3_goals_score_ave, month2_goals_score_ave, month1_goals_score_ave):
        setPlt(month6_goals_score_ave, month5_goals_score_ave, month4_goals_score_ave, month3_goals_score_ave, month2_goals_score_ave, month1_goals_score_ave)
        svg = plt2svg()
        plt.cla()
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response


    # y = [
    #     month6_goals_score_ave, month5_goals_score_ave, month4_goals_score_ave,
    #     month3_goals_score_ave, month2_goals_score_ave, month1_goals_score_ave
    #     ]

    # x = [
    #     month_count(5), month_count(4), month_count(3), month_count(2),
    #     month_count(1), month_count(0)
    #     ]

    # plt.plot(x, y, color='#00d5ff')
    # plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    # plt.xlabel("月")
    # plt.ylabel("目標評価平均")
    # fig = plt.figure()
    # ax = fig.add_subplot(111, xlabel='月', ylabel='目標評価平均')

    # ax.plot(df['H'])
    # ax.plot(goal_score_ave, 'rs:', label='HR', ms=10, mew=5, mec='green')
    # ax.plot(goal_score_ave, marker='^', linestyle='-.')

    # fig.savefig('goal_score.png')
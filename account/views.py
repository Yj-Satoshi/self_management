from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import login as auth_signin
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.views.generic import TemplateView
from django.views import View
from monthly_goal.models import MonthlyGoal
from weekly_action.models import WeeklyAction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

        auth_signin(request, form)


class MyPageView(UserPassesTestMixin, LoginRequiredMixin):
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

    def users_detail(request, user_id, *args, **kwargs):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id).exclude(sccore__isnull=False).order_by('year', 'month', 'goal')
        for goal in monthly_goals:
            weekly_actions = WeeklyAction.objects.filter(
                    monthly_goal_id=goal.id)
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 2)
        context = {
            'user': user,
            'monthly_goals': page_obj.object_list,
            'weekly_actions': weekly_actions,
            'page_obj': page_obj,
        }
        return render(
            request, 'account/main.html', context)

    def scored_users_detail(request, user_id):
        user = request.user
        monthly_goals = MonthlyGoal.objects.filter(
            custom_user_id=user.id, sccore__isnull=False).order_by('-year', '-month', 'goal')
        page_obj = MyPageView.paginate_queryset(request, monthly_goals, 2)
        context = {
            'user': user,
            'monthly_goals': page_obj.object_list,
            'page_obj': page_obj,
        }
        return render(
            request, 'account/main_scored.html', context)

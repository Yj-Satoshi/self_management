from django.urls import path, include
from . import views


app_name = 'monthly_goal'
urlpatterns = [
    path('', include('account.urls')),
    path(
        'goal/new/',
        views.MonthlyGoalCreateView.as_view(template_name='monthly_goal/goal_create.html'),
        name='goal-create'
    ),
    path(
        'goal/<int:pk>/', views.MonthlyGoalDetailView.as_view(
            template_name='monthly_goal/goal_detail.html'), name='goal-detail'
    ),
    path(
        'goal/<int:pk>/update', views.MonthlyGoalUpdateView.as_view(),
        name='goal-update'
    ),
    path(
        'goal/<int:pk>/delete', views.MonthlyGoalDeleteView.as_view(),
        name='goal-delete'
    ),
]

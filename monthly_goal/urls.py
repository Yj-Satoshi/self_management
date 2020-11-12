from django.urls import path
from . import views

app_name = 'monthly_goal'
urlpatterns = [
    path(
        'main/goal/new/',
        views.MonthlyGoalCreateView.as_view(template_name='monthly_goal/goal_create.html'),
        name='goal-create'
        ),
    path(
        'main/goal/<int:pk>/', views.MonthlyGoalDetailView.as_view(),
        name='goal-detail'
        ),
    path(
        'main/goal/<int:pk>/update', views.MonthlyGoalUpdateView.as_view(),
        name='goal-update'
        ),
    path(
        'main/goal/<int:pk>/delete', views.MonthlyGoalDeleteView.as_view(),
        name='goal-delete'
        ),
]

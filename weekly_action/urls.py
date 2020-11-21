from django.urls import path, include
from . import views


app_name = 'weekly_action'
urlpatterns = [
    path('', include('account.urls')),
    path(
        'goal/<int:monthly_goal_id>/action/new/',
        views.WeeklyActionCreateView.as_view(template_name='weekly_action/action_create.html'),
        name='action-create'
    ),
    path(
        'goal/<int:monthly_goal_id>/action/<int:pk>/', views.WeeklyActionDetailView.as_view(
            template_name='weekly_action/action_detail.html'), name='action-detail'
    ),
    path(
        'goal/<int:monthly_goal_id>/action/<int:pk>/update', views.WeeklyActionUpdateView.as_view(
            template_name='weekly_action/action_update.html'),
        name='action-update'
    ),
    path(
        'goal/<int:monthly_goal_id>/action/<int:pk>/delete', views.WeeklyActionDeleteView.as_view(
            template_name='weekly_action/action_delete.html'),
        name='action-delete'
    ),
]

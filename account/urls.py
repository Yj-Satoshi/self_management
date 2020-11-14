from django.urls import path
from . import views
from django.contrib.auth import views as views_auth

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views_auth.LoginView.as_view(template_name='account/index.html'), name='index'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    path(
        'main/<int:user_id>/', views.MyPageView.users_detail, name='main'
        ),
]

from django.urls import path
from . import views
from django.contrib.auth import views as views_auth

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views_auth.LoginView.as_view(template_name='account/index.html'), name='index'),
    path('account/', views.SignIn.as_view(), name='signin'),
    path('main/<int:pk>/', views.MainView.as_view(template_name='account/main.html'), name='main'),
]

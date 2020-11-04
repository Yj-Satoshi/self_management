from django.urls import path
from . import views
from django.contrib.auth import views as views_auth

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('', views.index, name='index'),
    path('', views_auth.LoginView.as_view(template_name='account/index.html'), name='signin'),
    # path('signout/', views.signout, name='signout'),
]

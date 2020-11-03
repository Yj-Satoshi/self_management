from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    # path('signout/', views.signout, name='signout'),
    # path('register/', views.register, name='register'),
]

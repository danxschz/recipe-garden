from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Main, name='main'),
    path('accounts/signup/', views.SignUp.as_view(), name="signup")
]
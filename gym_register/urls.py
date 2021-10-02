from django.urls import path, include
from .views import Home, SignUp
from django.contrib.auth import views

app_name = 'gym'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', SignUp.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),

]

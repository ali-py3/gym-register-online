from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Tuition
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, Http404
from django.contrib.auth.views import LoginView


# Create your views here.
class Home(ListView):
    template_name = 'GYM/home.html'
    queryset = Tuition.objects.all()

class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('gym:home')
    template_name = 'GYM/register.html'

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_authenticated:
            return reverse_lazy("gym:home")
        else:
            return reverse_lazy("gym:login")

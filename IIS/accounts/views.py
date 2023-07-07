from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView


class LoginUserView(LoginView):
    pass


class StartPageView(TemplateView):
    template_name = 'accounts/start_page.html'


def logout_user(request):
    logout(request)
    return redirect('login')

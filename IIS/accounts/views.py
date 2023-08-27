from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from people.models import Person


class LoginUserView(LoginView):
    pass


# class StartPageView(TemplateView):
#     template_name = 'accounts/start_page.html'


def profile(request):
    return HttpResponseRedirect(
        reverse_lazy('person_detail', kwargs={'pk': Person.objects.get(user_instance=request.user).id}))


def logout_user(request):
    logout(request)
    return redirect('login')

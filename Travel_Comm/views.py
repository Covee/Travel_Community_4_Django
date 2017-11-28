from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):
    template_name = 'Travel_Comm/home.html'


class LoginView(TemplateView):
	template_name = 'registration/login.html'


# 로그인 인증기능
class CreateUserView(CreateView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('register_done')


class RegisteredView(TemplateView):
    template_name = 'registration/register_done.html'

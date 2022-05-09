from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from doc_filler.apps.users.forms import CreateUserForm, UserAuthenticationForm
from doc_filler.apps.users.user_testers import UserIsUserHimselfOrAdmin


class CreateUserView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'doc_filler/users/create_user.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Пользователь зарегистрирован')
        return reverse('login')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.add_message(self.request, messages.INFO, 'Вы уже вошли')
            return redirect(reverse('home'))
        return super(CreateUserView, self).post(request, *args, **kwargs)


class UpdateUserView(UserIsUserHimselfOrAdmin, generic.UpdateView):
    form_class = CreateUserForm
    template_name = 'doc_filler/users/update_user.html'
    model = get_user_model()
    no_access_message = 'Нельзя редактировать других пользователей'
    no_access_redirect_url = reverse_lazy('home')

    def get_success_url(self):
        update_session_auth_hash(
            self.request,
            *get_user_model().objects.filter(pk=self.request.user.pk),
        )
        messages.add_message(self.request, messages.INFO, 'Данные обновлены')
        return reverse('home')


class UserLoginView(LoginView):
    template_name = 'doc_filler/login.html'
    form_class = UserAuthenticationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Вы вошли')
        return reverse('home')


class UserLogoutView(LogoutView):

    def get_next_page(self):
        messages.add_message(self.request, messages.INFO, 'Вы вышли')
        return reverse('home')

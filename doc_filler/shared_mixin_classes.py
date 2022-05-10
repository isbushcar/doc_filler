from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def get_login_url(self):
        messages.add_message(self.request, messages.INFO, 'Сначала войдите')
        return reverse('login')

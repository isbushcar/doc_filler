from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserIsUserHimselfOrAdmin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.kwargs['pk'] or self.request.user.is_superuser

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            self.no_access_message += '. ' + _('TryToLoginFirst')
        messages.add_message(self.request, messages.INFO, self.no_access_message)
        return redirect(self.no_access_redirect_url)


class UserIsAuthorOrAdmin(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.id == self.model.objects.filter(pk=self.kwargs['pk'])[0].author.pk:
            return True
        return True if self.request.user.is_superuser else False

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            self.no_access_message += '. ' + _('TryToLoginFirst')
        messages.add_message(self.request, messages.INFO, self.no_access_message)
        return redirect(self.no_access_redirect_url)

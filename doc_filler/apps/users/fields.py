from django.contrib.auth.forms import UsernameField


class UsernameFieldWithPlaceholder(UsernameField):

    def widget_attrs(self, widget):
        return {
            **super(UsernameFieldWithPlaceholder, self).widget_attrs(widget),
            'placeholder': 'Имя пользователя',
            'class': 'form-control',
        }

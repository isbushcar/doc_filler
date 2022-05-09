from django.contrib.auth.models import User

# Change default user __str__ method
User.add_to_class('__str__', lambda self: f'{self.first_name} {self.last_name}')

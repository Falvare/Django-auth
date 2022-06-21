from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions', 'is_active', 'date_joined', 'password']
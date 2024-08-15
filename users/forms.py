from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
        help_texts = {
            "password1": "Пароль должен содержать более 8 символов, содержать буквы верхнего и нижнего регистра, и содержать хотя бы одну цифру.",
            "password2": "Пароли не совпадают.",
        }
        labels = {
            "email": "Электронная почта",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }

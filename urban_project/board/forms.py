from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Advertisement


# Форма для создания и редактирования объявлений
class AdvertisementForm(forms.ModelForm):
    """
    Форма для создания и редактирования объявлений.

    Атрибуты:
        Meta (class): Вложенный класс, определяющий модель и поля для формы.
    """

    class Meta:
        model = Advertisement
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Изображение',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'placeholder': 'Введите содержание'}),
        }


# Форма для регистрации нового пользователя
class SignUpForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.

    Attributes:
        Meta (class): Вложенный класс, определяющий модель и поля для формы.
    """

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

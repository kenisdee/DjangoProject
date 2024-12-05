from django.contrib.auth.models import User
from django.db import models


# Модель для объявления
class Advertisement(models.Model):
    """
    Модель для хранения объявлений.

    Атрибуты:
        title (CharField): Заголовок объявления.
        content (TextField): Содержание объявления.
        author (ForeignKey): Автор объявления (связь с моделью User).
        created_at (DateTimeField): Дата и время создания объявления.
        image (ImageField): Изображение, связанное с объявлением.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='advertisements/', null=True, blank=True)

    def __str__(self):
        return self.title


# Модель для комментариев к объявлениям
class Comment(models.Model):
    """
    Модель для хранения комментариев к объявлениям.

    Атрибуты:
        advertisement (ForeignKey): Объявление, к которому относится комментарий (связь с моделью Advertisement).
        author (ForeignKey): Автор комментария (связь с моделью User).
        content (TextField): Содержание комментария.
        created_at (DateTimeField): Дата и время создания комментария.
    """
    advertisement = models.ForeignKey(Advertisement, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.advertisement}'

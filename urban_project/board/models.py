import os

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
        likes (PositiveIntegerField): Количество лайков.
        dislikes (PositiveIntegerField): Количество дизлайков.
        liked_by (ManyToManyField): Пользователи, которые поставили лайк.
        disliked_by (ManyToManyField): Пользователи, которые поставили дизлайк.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='advertisements/', null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_advertisements', blank=True)
    disliked_by = models.ManyToManyField(User, related_name='disliked_advertisements', blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Удаляем изображение из файловой системы
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(Advertisement, self).delete(*args, **kwargs)


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


class UserProfile(models.Model):
    """
    Модель профиля пользователя для хранения дополнительной статистики.

    Атрибуты:
        user (OneToOneField): Связь с моделью User.
        advertisement_count (PositiveIntegerField): Количество созданных объявлений.
        like_count (PositiveIntegerField): Количество лайков.
        dislike_count (PositiveIntegerField): Количество дизлайков.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advertisement_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Возвращает строковое представление профиля пользователя."""
        return self.user.username

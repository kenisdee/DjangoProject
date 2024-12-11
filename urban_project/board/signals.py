from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Advertisement, UserProfile


@receiver(post_save, sender=Advertisement)
def update_advertisement_count(sender, instance, created, **kwargs):
    """
    Сигнал для обновления количества созданных объявлений.

    Args:
        sender (Model): Модель, которая отправила сигнал.
        instance (Advertisement): Экземпляр созданного объявления.
        created (bool): Флаг, указывающий, был ли объект создан.
    """
    if created:
        profile, _ = UserProfile.objects.get_or_create(user=instance.author)
        profile.advertisement_count += 1
        profile.save()


@receiver(post_delete, sender=Advertisement)
def decrement_advertisement_count(sender, instance, **kwargs):
    """
    Сигнал для уменьшения количества созданных объявлений при удалении.

    Args:
        sender (Model): Модель, которая отправила сигнал.
        instance (Advertisement): Экземпляр удаляемого объявления.
    """
    profile, _ = UserProfile.objects.get_or_create(user=instance.author)
    profile.advertisement_count -= 1
    profile.like_count -= instance.liked_by.count()  # Убираем лайки
    profile.dislike_count -= instance.disliked_by.count()  # Убираем дизлайки
    profile.save()


@receiver(post_save, sender=Advertisement)
def update_like_dislike_count(sender, instance, **kwargs):
    """
    Сигнал для обновления количества лайков и дизлайков.

    Args:
        sender (Model): Модель, которая отправила сигнал.
        instance (Advertisement): Экземпляр объявления.
    """
    profile, _ = UserProfile.objects.get_or_create(user=instance.author)
    profile.like_count = instance.liked_by.count()
    profile.dislike_count = instance.disliked_by.count()
    profile.save()

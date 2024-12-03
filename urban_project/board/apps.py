from django.apps import AppConfig


# Конфигурация приложения "board"
class BoardConfig(AppConfig):
    """
    Конфигурация приложения "board".

    Attributes:
        default_auto_field (str): Тип поля для автоматического создания первичных ключей.
        name (str): Имя приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

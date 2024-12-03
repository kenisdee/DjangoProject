"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Запуск административных задач."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, что он установлен и "
            "доступен в вашей переменной окружения PYTHONPATH? Возможно, вы "
            "забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
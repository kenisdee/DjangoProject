from django.contrib import admin

from .models import Advertisement, Comment

# Регистрация моделей в админ-панели
admin.site.register(Advertisement)
admin.site.register(Comment)

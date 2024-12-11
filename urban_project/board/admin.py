from django.contrib import admin
from .models import UserProfile
from .models import Advertisement, Comment

# Регистрация моделей в админ-панели
admin.site.register(Advertisement)
admin.site.register(Comment)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'advertisement_count', 'like_count', 'dislike_count')
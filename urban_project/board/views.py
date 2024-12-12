import os

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AdvertisementForm
from .forms import SignUpForm
from .models import Advertisement
from .utils import resize_image
from .signals import update_like_dislike_count

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Функция для выхода пользователя
def logout_view(request):
    """
    Выход пользователя и перенаправление на домашнюю страницу.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Перенаправление на домашнюю страницу.
    """
    logout(request)
    return redirect('home')


# Функция для регистрации нового пользователя
def signup(request):
    """
    Обработка регистрации нового пользователя.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отображение формы регистрации или перенаправление на страницу объявлений после успешной регистрации.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Функция для отображения домашней страницы
def home(request):
    """
    Отображение домашней страницы.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отображение домашней страницы.
    """
    return render(request, 'home.html')


# Функция для отображения списка объявлений
def advertisement_list(request):
    """
    Отображение списка объявлений.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отображение списка объявлений.
    """
    advertisements = Advertisement.objects.all()
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})


# Функция для отображения деталей конкретного объявления
def advertisement_detail(request, pk):
    """
    Отображение деталей конкретного объявления.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        pk (int): Первичный ключ объявления.

    Returns:
        HttpResponse: Отображение деталей объявления.
    """
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})


# Функция для добавления нового объявления (только для аутентифицированных пользователей)
@login_required
def add_advertisement(request):
    """
    Обработка добавления нового объявления.

    Аргументы:
        request (HttpRequest): Объект HTTP-запроса.

    Возвращает:
        HttpResponse: Отображение формы для добавления объявления или перенаправление на список объявлений после успешного добавления.
    """
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user

            # Уменьшаем изображение
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
                with open(image_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)
                resize_image(image_path)
                advertisement.image = image_file.name

            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})


# Функция для редактирования существующего объявления (только для аутентифицированных пользователей)
@login_required
def edit_advertisement(request, pk):
    """
    Обработка редактирования существующего объявления.

    Аргументы:
        request (HttpRequest): Объект HTTP-запроса.
        pk (int): Первичный ключ объявления.

    Возвращает:
        HttpResponse: Отображение формы для редактирования объявления или перенаправление на детали объявления после успешного редактирования.
    """
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            advertisement = form.save(commit=False)

            # Уменьшаем изображение
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
                with open(image_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)
                resize_image(image_path)
                advertisement.image = image_file.name

            advertisement.save()
            return redirect('board:advertisement_detail', pk=advertisement.pk)
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html', {'form': form})


# Функция для удаления существующего объявления (только для аутентифицированных пользователей)
@login_required
def delete_advertisement(request, pk):
    """
    Обработка удаления существующего объявления.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        pk (int): Первичный ключ объявления.

    Returns:
        HttpResponse: Отображение формы подтверждения удаления объявления или перенаправление на список объявлений после успешного удаления.
    """
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.user != advertisement.author:
        return redirect('board:advertisement_list')  # Перенаправление, если пользователь не является автором

    if request.method == 'POST':
        advertisement.delete()
        return redirect('board:advertisement_list')

    return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})


@login_required
def like_advertisement(request, pk):
    """
    Обработка лайка объявления.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        pk (int): Первичный ключ объявления.

    Returns:
        HttpResponse: Перенаправление на детали объявления после лайка.
    """
    advertisement = get_object_or_404(Advertisement, pk=pk)
    user = request.user

    if user in advertisement.disliked_by.all():
        advertisement.disliked_by.remove(user)
        advertisement.dislikes -= 1

    if user in advertisement.liked_by.all():
        advertisement.liked_by.remove(user)
        advertisement.likes -= 1
    else:
        advertisement.liked_by.add(user)
        advertisement.likes += 1

    advertisement.save()

    # Обновляем статистику
    update_like_dislike_count(sender=Advertisement, instance=advertisement)

    return redirect('board:advertisement_detail', pk=advertisement.pk)

@login_required
def dislike_advertisement(request, pk):
    """
    Обработка дизлайка объявления.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        pk (int): Первичный ключ объявления.

    Returns:
        HttpResponse: Перенаправление на детали объявления после дизлайка.
    """
    advertisement = get_object_or_404(Advertisement, pk=pk)
    user = request.user

    if user in advertisement.liked_by.all():
        advertisement.liked_by.remove(user)
        advertisement.likes -= 1

    if user in advertisement.disliked_by.all():
        advertisement.disliked_by.remove(user)
        advertisement.dislikes -= 1
    else:
        advertisement.disliked_by.add(user)
        advertisement.dislikes += 1

    advertisement.save()

    # Обновляем статистику
    update_like_dislike_count(sender=Advertisement, instance=advertisement)

    return redirect('board:advertisement_detail', pk=advertisement.pk)

def advertisement_list(request):
    """
    Отображение списка объявлений с пагинацией.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отображение списка объявлений с пагинацией.
    """
    # Получаем все объявления
    advertisements = Advertisement.objects.all().order_by('-created_at')

    # Пагинация
    paginator = Paginator(advertisements, 5)
    page = request.GET.get('page')

    try:
        # Получаем объявления для текущей страницы
        advertisements_page = paginator.page(page)
    except PageNotAnInteger:
        # Если page не является числом, показываем первую страницу
        advertisements_page = paginator.page(1)
    except EmptyPage:
        # Если page находится за пределами диапазона, показываем последнюю страницу
        advertisements_page = paginator.page(paginator.num_pages)

    return render(request, 'board/advertisement_list.html', {
        'advertisements_page': advertisements_page,
    })
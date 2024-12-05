from board.forms import AdvertisementForm
from board.models import Advertisement
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AdvertisementForm
from .forms import SignUpForm
from .models import Advertisement


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
            form.save()
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

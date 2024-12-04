### `README.md`


# Django Advertisement Board

Этот проект представляет собой простое веб-приложение на Django для управления объявлениями. Пользователи могут
просматривать, добавлять, редактировать и удалять объявления.

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/kenisdee/DjangoProject.git
   cd DjangoProject
   ```

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate  # Для Windows
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Перейдите в папку с проектом:**

   ```bash
   cd urban_project
   ```


5. **Выполните миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Создайте суперпользователя (опционально):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```

8. **Откройте приложение в браузере:**

   Перейдите по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Примеры работы

### Добавление объявления

1. **Перейдите на страницу добавления объявления:**

   [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/)

2. **Заполните форму и нажмите "Submit":**

   ```html
   <form method="post">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Submit</button>
   </form>
   ```

### Редактирование объявления

1. **Перейдите на страницу редактирования объявления:**

   [http://127.0.0.1:8000/advertisement/1/edit/](http://127.0.0.1:8000/advertisement/1/edit/)

2. **Измените данные и нажмите "Save changes":**

   ```html
   <form method="post">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Save changes</button>
   </form>
   ```

### Удаление объявления

1. **Перейдите на страницу удаления объявления:**

   [http://127.0.0.1:8000/advertisement/1/delete/](http://127.0.0.1:8000/advertisement/1/delete/)

2. **Подтвердите удаление:**

   ```html
   <form method="post">
       {% csrf_token %}
       <button type="submit">Удалить</button>
       <a href="{% url 'board:advertisement_detail' pk=advertisement.pk %}">Отмена</a>
   </form>
   ```

## Структура проекта

- **board/**: Приложение для управления объявлениями.
    - **migrations/**: Миграции базы данных.
    - **templates/board/**: Шаблоны для отображения объявлений.
    - **admin.py**: Регистрация моделей в админ-панели.
    - **forms.py**: Формы для объявлений и регистрации.
    - **models.py**: Модели для объявлений и комментариев.
    - **urls.py**: URL-шаблоны для приложения.
    - **views.py**: Представления для обработки запросов.
- **urban_project/**: Основной конфигурационный файл проекта.
    - **settings.py**: Настройки проекта.
    - **urls.py**: Основные URL-шаблоны проекта.
- **manage.py**: Утилита командной строки Django для управления проектом.
- **requirements.txt**: Зависимости проекта.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE.md).

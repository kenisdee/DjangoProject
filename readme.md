# Django Advertisement Board

<img width="1228" alt="Снимок экрана 2024-12-04 в 17 54 46" src="https://github.com/user-attachments/assets/66737438-ebb2-4195-b272-3e3aa9ca63fc">

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

   [http://127.0.0.1:8000/board/add/](http://127.0.0.1:8000/board/add/)

2. **Заполните форму и нажмите "Submit":**

<img width="411" alt="Снимок экрана 2024-12-04 в 17 57 03" src="https://github.com/user-attachments/assets/f0fe76e1-3370-446e-bb81-26e66d898417">


### Редактирование объявления

1. **Перейдите на страницу редактирования объявления:**

   [http://127.0.0.1:8000/board/advertisement/1/edit/](http://127.0.0.1:8000/board/advertisement/1/edit/)

2. **Измените данные и нажмите "Save changes":**

<img width="410" alt="Снимок экрана 2024-12-04 в 17 59 17" src="https://github.com/user-attachments/assets/85be7f43-7e0e-4655-a9f3-ee32d8e4f874">

### Удаление объявления

1. **Перейдите на страницу удаления объявления:**

   [http://127.0.0.1:8000/board/advertisement/1/delete/](http://127.0.0.1:8000/board/advertisement/1/delete/)

2. **Подтвердите удаление:**

<img width="436" alt="Снимок экрана 2024-12-04 в 18 00 09" src="https://github.com/user-attachments/assets/52203acb-f1c9-46d4-868e-3766eb4113e4">

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

# Проект API для Yatube

Проект социальной сети с публикациями, комментариями, группами и подписками.

## О проекте

Это REST API для социальной сети Yatube, реализованное на Django REST Framework. API предоставляет функционал для:

- Публикации постов
- Комментирования
- Создания групп
- Подписки на авторов
- Аутентификации через JWT-токены

## Технологии

- **Python** + **Django** - бэкенд
- **Django REST Framework** - API
- **Simple JWT** - аутентификация
- **Djoser** - управление пользователями

# Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
Windows:
python -m venv venv
```

```
source .venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
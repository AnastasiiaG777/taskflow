# TaskFlow Team Tracker

Веб-приложение для управления задачами команды, созданное на Django.

## Возможности

- Регистрация и авторизация пользователей
- Создание задач
- Редактирование задач
- Удаление задач
- Изменение статуса задач
- Поиск задач
- Фильтрация по статусу
- Пагинация
- Разделение задач по пользователям
- Отображение даты создания и обновления задач

## Стек технологий

- Python 3
- Django 6
- SQLite
- Bootstrap 5
- HTML/CSS

## AI-инструменты

Во время разработки использовались AI-инструменты:
- ChatGPT
- OpenCode

AI использовался для:
- генерации структуры проекта;
- ускорения написания кода;
- улучшения UI;
- настройки деплоя;
- оптимизации логики приложения.

## Запуск проекта локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/AnastasiiaG777/taskflow.git
```

### 2. Перейти в папку проекта

```bash
cd taskflow
```

### 3. Создать виртуальное окружение

```bash
python -m venv .venv
```

### 4. Активировать виртуальное окружение

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 5. Установить зависимости

```bash
pip install -r requirements.txt
```

### 6. Выполнить миграции

```bash
python manage.py migrate
```

### 7. Запустить сервер

```bash
python manage.py runserver
```

## Деплой

Проект задеплоен на Render:

https://taskflow-c9wr.onrender.com

## GitHub

Репозиторий проекта:

https://github.com/AnastasiiaG777/taskflow
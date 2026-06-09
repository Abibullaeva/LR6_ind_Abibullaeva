# ==============================================
# БЛОК ПОДКЛЮЧЕНИЯ БИБЛИОТЕК
# ==============================================
import os
from pathlib import Path  # Для кроссплатформенной работы с путями

# ==============================================
# БЛОК ОПРЕДЕЛЕНИЯ БАЗОВЫХ ПУТЕЙ
# ==============================================
BASE_DIR = Path(__file__).resolve().parent.parent  # Корневая папка проекта

# ==============================================
# БЛОК БЕЗОПАСНОСТИ (СЕКРЕТНЫЙ КЛЮЧ)
# ==============================================
SECRET_KEY = 'django-insecure-4ju2n@$f9d0c=h)_g0lbb%k9&@rf(xa$d$g$&5ri$uf)*gev^4'
# Секретный ключ для криптографической подписи сессий и CSRF-токенов

# ==============================================
# БЛОК РЕЖИМА ОТЛАДКИ
# ==============================================
DEBUG = True
# True — при ошибках показывается детальная информация (только для разработки!)

# ==============================================
# БЛОК ДОПУЩЕННЫХ ХОСТОВ
# ==============================================
ALLOWED_HOSTS = ['*']
# Разрешает подключения с любых IP-адресов (для Docker/Replit)

# ==============================================
# БЛОК ЗАРЕГИСТРИРОВАННЫХ ПРИЛОЖЕНИЙ
# ==============================================
INSTALLED_APPS = [
    'django.contrib.admin',      # Админ-панель Django
    'django.contrib.auth',       # Система аутентификации
    'django.contrib.contenttypes', # Работа с типами контента
    'django.contrib.sessions',   # Управление сессиями
    'django.contrib.messages',   # Система сообщений
    'django.contrib.staticfiles', # Обработка статических файлов
    'tasks.apps.TasksConfig',    # НАШЕ ПРИЛОЖЕНИЕ (контейнер безопасности)
]

# ==============================================
# БЛОК ПРОМЕЖУТОЧНОГО ПО (MIDDLEWARE)
# ==============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',      # Заголовки безопасности
    'django.contrib.sessions.middleware.SessionMiddleware', # Управление сессиями
    'django.middleware.common.CommonMiddleware',         # Обработка слешей и пр.
    'django.middleware.csrf.CsrfViewMiddleware',         # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Привязка пользователя
    'django.contrib.messages.middleware.MessageMiddleware',   # Обработка сообщений
]

# ==============================================
# БЛОК МАРШРУТИЗАЦИИ (URL-КОНФИГУРАЦИЯ)
# ==============================================
ROOT_URLCONF = 'django_project.urls'
# Указывает файл, где описаны все URL-адреса сайта

# ==============================================
# БЛОК НАСТРОЙКИ ШАБЛОНОВ
# ==============================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Дополнительные папки с шаблонами (пусто — ищем в папках приложений)
        'APP_DIRS': True,  # Искать шаблоны в папке templates каждого приложения
        'OPTIONS': {
            'context_processors': [  # Процессоры, добавляющие переменные во все шаблоны
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==============================================
# БЛОК ТОЧКИ ВХОДА WSGI
# ==============================================
WSGI_APPLICATION = 'django_project.wsgi.application'
# Используется веб-серверами (Gunicorn, uWSGI) для запуска приложения

# ==============================================
# БЛОК НАСТРОЙКИ БАЗЫ ДАННЫХ
# ==============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Движок SQLite (легковесный)
        'NAME': BASE_DIR / 'db.sqlite3',         # Путь к файлу БД
    }
}

# ==============================================
# БЛОК ВАЛИДАЦИИ ПАРОЛЕЙ
# ==============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================================
# БЛОК ЛОКАЛИЗАЦИИ (ЯЗЫК И ВРЕМЯ)
# ==============================================
LANGUAGE_CODE = 'en-us'      # Язык интерфейса
TIME_ZONE = 'UTC'            # Часовой пояс
USE_I18N = True              # Включить интернационализацию
USE_TZ = True                # Использовать часовые пояса в БД

# ==============================================
# БЛОК СТАТИЧЕСКИХ ФАЙЛОВ
# ==============================================
STATIC_URL = 'static/'       # URL-префикс для статики (CSS, JS, изображения)

# ==============================================
# БЛОК ПЕРВИЧНОГО КЛЮЧА
# ==============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Тип автоинкрементного поля для моделей (64-битный целый тип)

# ==============================================
# БЛОК НАСТРОЕК HTTPS (ЗАКОММЕНТИРОВАН ДЛЯ Replit) для ДЗ№8
# ==============================================
# ВНИМАНИЕ: Этот блок НЕ активен, так как закомментирован.
# Он предназначен для принудительного HTTPS в продакшн-среде.

# SESSION_COOKIE_SECURE = True          # Передавать cookie сессии только по HTTPS
# CSRF_COOKIE_SECURE = True             # Передавать CSRF-токен только по HTTPS
# SECURE_HSTS_SECONDS = 31536000        # Включить HSTS на 1 год
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True # HSTS для поддоменов
# SECURE_HSTS_PRELOAD = True            # Разрешить предзагрузку HSTS
# SECURE_BROWSER_XSS_FILTER = True      # Включить XSS-фильтр браузера
# SECURE_CONTENT_TYPE_NOSNIFF = True    # Запретить MIME-сниффинг
# X_FRAME_OPTIONS = 'DENY'              # Запретить встраивание в iframe
# SECURE_SSL_REDIRECT = True            # (ЗАКОММЕНТИРОВАНО) — Replit сам перенаправляет
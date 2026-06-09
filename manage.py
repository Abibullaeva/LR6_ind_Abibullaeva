#!/usr/bin/env python
# Шебанг (shebang) – указывает путь к интерпретатору Python.
# Позволяет запускать файл как исполняемый скрипт без явного вызова `python manage.py`.

"""Django's command-line utility for administrative tasks."""
# Строка документации (docstring), описывающая назначение файла.
# Данный файл является утилитой командной строки Django для выполнения административных задач.

import os
# Импорт модуля `os` для работы с переменными окружения и файловой системой.
# В данном файле используется для установки переменной окружения `DJANGO_SETTINGS_MODULE`.

import sys
# Импорт модуля `sys` для доступа к аргументам командной строки (`sys.argv`).
# Позволяет передавать команды в Django (например, `runserver`, `migrate`, `makemigrations`).


def main():
    """Run administrative tasks."""
    # Главная функция, которая запускает административные задачи Django.
    # Вызывается при запуске скрипта.

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    # Устанавливает переменную окружения `DJANGO_SETTINGS_MODULE`, если она ещё не задана.
    # Эта переменная указывает Django, какой файл настроек (`settings.py`) использовать.
    # `django_project.settings` – путь к файлу настроек относительно корня проекта.

    try:
        from django.core.management import execute_from_command_line
        # Попытка импортировать функцию `execute_from_command_line` из модуля Django.
        # Эта функция запускает команды, переданные через командную строку (например, `runserver`).
    except ImportError as exc:
        # Если Django не установлен, возникает ошибка `ImportError`.
        # В этом случае выводится понятное сообщение об ошибке.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # `from exc` сохраняет исходную ошибку в цепочке исключений для отладки.

    execute_from_command_line(sys.argv)
    # Запускает команду, переданную через командную строку.
    # `sys.argv` – список аргументов командной строки.
    # Например, при запуске `python manage.py runserver`:
    #   sys.argv[0] = 'manage.py'
    #   sys.argv[1] = 'runserver'
    #   execute_from_command_line обрабатывает эти аргументы и запускает сервер.


if __name__ == '__main__':
    # Условная конструкция, которая проверяет, запущен ли файл непосредственно как скрипт.
    # Если файл импортирован как модуль (например, `import manage`), код внутри не выполняется.
    # Если файл запущен напрямую (`python manage.py`), вызывается функция `main()`.
    main()
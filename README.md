Учебный проект на Python с использованием Django 5.0, посвящённый настройке конфигурации проекта, автоматизации проверки структуры и расчёту трудоёмкости программного обеспечения.

Содержание проекта

django_project/ — структура Django-проекта.

tasks/ — дополнительные задачи проекта.

ansible_demo.yml — демонстрация автоматизации проверки структуры проекта и формирования отчёта.

config_report.txt — отчёт о конфигурации проекта.

test_https_config.py — реализация расчётов трудоёмкости по моделям COCOMO и COCOMO II.

pyproject.toml — настройки проекта и зависимости.

Технологии

Python 3.10+, Django 5.0, Poetry, Ansible.

Установка и запуск

git clone https://github.com/Abibullaeva/LR6_ind_Abibullaeva.git
cd LR6_ind_Abibullaeva
poetry install

Запуск Django:

python manage.py runserver

Запуск расчётов COCOMO:

python test_https_config.py

Запуск Ansible:

ansible-playbook ansible_demo.yml

Назначение

Репозиторий содержит учебные материалы и программные решения для изучения Django, автоматизации конфигурации и оценки трудоёмкости разработки программного обеспечения.

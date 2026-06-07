"""
Программа для автоматизированного расчёта трудоёмкости по модели COCOMO
Разработана для лабораторной работы №13
Режим работы: интерактивный (запрос данных у пользователя)
"""

import math

def calculate_cocomo(KDSI, project_type, M=1.0):
    """
    Расчёт трудоёмкости (PM) по алгоритмической модели COCOMO
    project_type: 'organic' - простой, 'semidetached' - средний, 'embedded' - сложный
    """
    if project_type == 'organic':
        PM = 2.4 * (KDSI ** 1.05) * M
    elif project_type == 'semidetached':
        PM = 3.0 * (KDSI ** 1.12) * M
    elif project_type == 'embedded':
        PM = 3.6 * (KDSI ** 1.20) * M
    else:
        raise ValueError("Неизвестный тип проекта")
    return PM

def calculate_TDEV(PM):
    """Расчёт длительности проекта (TDEV) в месяцах"""
    return 2.5 * (PM ** 0.38)

def calculate_average_staff(PM, TDEV):
    """Расчёт средней численности персонала"""
    return PM / TDEV

def calculate_by_object_points(NOP, reuse_percent, PROD):
    """Расчёт трудоёмкости по методу объектных точек"""
    return (NOP * (1 - reuse_percent / 100)) / PROD

def main():
    print("=" * 60)
    print("АВТОМАТИЗИРОВАННЫЙ РАСЧЁТ ПО МОДЕЛИ COCOMO")
    print("Программа для технико-экономического обоснования проектов")
    print("=" * 60)

    print("\nВВОД ИСХОДНЫХ ДАННЫХ")
    print("-" * 40)

    # Ввод данных для алгоритмической модели
    print("\n--- Алгоритмическая модель (на основе строк кода) ---")
    KDSI = float(input("Введите количество строк кода (в тысячах, KDSI): "))
    print("Выберите тип проекта:")
    print("1 - Простой (органический)")
    print("2 - Средней сложности")
    print("3 - Сложный (встроенный)")
    project_choice = input("Ваш выбор (1/2/3): ")

    if project_choice == '1':
        project_type = 'organic'
        print("   Выбран: Простой проект")
    elif project_choice == '2':
        project_type = 'semidetached'
        print("   Выбран: Проект средней сложности")
    elif project_choice == '3':
        project_type = 'embedded'
        print("   Выбран: Сложный проект")
    else:
        project_type = 'organic'
        print("   Неверный выбор. Принят тип: Простой проект")

    M = float(input("Введите значение множителя M (учёт характеристик проекта): "))

    # Ввод данных для метода объектных точек
    print("\n--- Метод объектных точек (COCOMO II) ---")
    NOP = float(input("Введите количество объектных точек (NOP): "))
    reuse_percent = float(input("Введите долю повторного использования (%): "))
    PROD = float(input("Введите производительность (объектных точек/месяц, PROD): "))

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ РАСЧЁТА")
    print("=" * 60)

    # Расчёт по алгоритмической модели
    PM_algo = calculate_cocomo(KDSI, project_type, M)
    TDEV_algo = calculate_TDEV(PM_algo)
    staff_algo = calculate_average_staff(PM_algo, TDEV_algo)

    print(f"\n1. Алгоритмическая модель COCOMO (тип: {project_type})")
    print(f"   Трудоёмкость (PM):        {PM_algo:.2f} человеко-месяцев")
    print(f"   Длительность проекта:     {TDEV_algo:.2f} месяцев (≈ {TDEV_algo * 4:.0f} недель)")
    print(f"   Средняя численность:      {staff_algo:.2f} человека")

    # Расчёт по методу объектных точек
    PM_object = calculate_by_object_points(NOP, reuse_percent, PROD)
    TDEV_object = calculate_TDEV(PM_object)
    staff_object = calculate_average_staff(PM_object, TDEV_object)

    print(f"\n2. Метод объектных точек COCOMO II")
    print(f"   Трудоёмкость (PM):        {PM_object:.2f} человеко-месяцев")
    print(f"   Длительность проекта:     {TDEV_object:.2f} месяцев")
    print(f"   Средняя численность:      {staff_object:.2f} человека")

    print("\n" + "=" * 60)
    print("РАСЧЁТ ЗАВЕРШЁН")
    print("=" * 60)

if __name__ == "__main__":
    main()
    
# import os
# import sys
# import django

# # Указываем настройки проекта
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# # Настраиваем Django
# django.setup()

# from django.conf import settings
# import unittest


# class TestHTTPSConfig(unittest.TestCase):
#     """Тесты проверки наличия обязательных HTTPS-настроек в settings.py"""

#     def test_session_cookie_secure(self):
#         """SESSION_COOKIE_SECURE должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'SESSION_COOKIE_SECURE', False),
#             "SESSION_COOKIE_SECURE должен быть True"
#         )

#     def test_csrf_cookie_secure(self):
#         """CSRF_COOKIE_SECURE должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'CSRF_COOKIE_SECURE', False),
#             "CSRF_COOKIE_SECURE должен быть True"
#         )

#     def test_hsts_configured(self):
#         """SECURE_HSTS_SECONDS должен быть больше 0"""
#         hsts = getattr(settings, 'SECURE_HSTS_SECONDS', 0)
#         self.assertGreater(
#             hsts, 0,
#             "SECURE_HSTS_SECONDS должен быть больше 0"
#         )

#     def test_hsts_include_subdomains(self):
#         """SECURE_HSTS_INCLUDE_SUBDOMAINS должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'SECURE_HSTS_INCLUDE_SUBDOMAINS', False),
#             "SECURE_HSTS_INCLUDE_SUBDOMAINS должен быть True"
#         )

#     def test_hsts_preload(self):
#         """SECURE_HSTS_PRELOAD должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'SECURE_HSTS_PRELOAD', False),
#             "SECURE_HSTS_PRELOAD должен быть True"
#         )

#     def test_x_frame_options_deny(self):
#         """X_FRAME_OPTIONS должен быть 'DENY'"""
#         self.assertEqual(
#             getattr(settings, 'X_FRAME_OPTIONS', ''),
#             'DENY',
#             "X_FRAME_OPTIONS должен быть 'DENY'"
#         )

#     def test_secure_browser_xss_filter(self):
#         """SECURE_BROWSER_XSS_FILTER должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'SECURE_BROWSER_XSS_FILTER', False),
#             "SECURE_BROWSER_XSS_FILTER должен быть True"
#         )

#     def test_secure_content_type_nosniff(self):
#         """SECURE_CONTENT_TYPE_NOSNIFF должен быть True"""
#         self.assertTrue(
#             getattr(settings, 'SECURE_CONTENT_TYPE_NOSNIFF', False),
#             "SECURE_CONTENT_TYPE_NOSNIFF должен быть True"
#         )


# if __name__ == '__main__':
#     # Запуск тестов с подробным выводом
#     unittest.main(verbosity=2)


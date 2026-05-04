import os
import sys
import django

# Указываем настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# Настраиваем Django
django.setup()

from django.conf import settings
import unittest


class TestHTTPSConfig(unittest.TestCase):
    """Тесты проверки наличия обязательных HTTPS-настроек в settings.py"""

    def test_session_cookie_secure(self):
        """SESSION_COOKIE_SECURE должен быть True"""
        self.assertTrue(
            getattr(settings, 'SESSION_COOKIE_SECURE', False),
            "SESSION_COOKIE_SECURE должен быть True"
        )

    def test_csrf_cookie_secure(self):
        """CSRF_COOKIE_SECURE должен быть True"""
        self.assertTrue(
            getattr(settings, 'CSRF_COOKIE_SECURE', False),
            "CSRF_COOKIE_SECURE должен быть True"
        )

    def test_hsts_configured(self):
        """SECURE_HSTS_SECONDS должен быть больше 0"""
        hsts = getattr(settings, 'SECURE_HSTS_SECONDS', 0)
        self.assertGreater(
            hsts, 0,
            "SECURE_HSTS_SECONDS должен быть больше 0"
        )

    def test_hsts_include_subdomains(self):
        """SECURE_HSTS_INCLUDE_SUBDOMAINS должен быть True"""
        self.assertTrue(
            getattr(settings, 'SECURE_HSTS_INCLUDE_SUBDOMAINS', False),
            "SECURE_HSTS_INCLUDE_SUBDOMAINS должен быть True"
        )

    def test_hsts_preload(self):
        """SECURE_HSTS_PRELOAD должен быть True"""
        self.assertTrue(
            getattr(settings, 'SECURE_HSTS_PRELOAD', False),
            "SECURE_HSTS_PRELOAD должен быть True"
        )

    def test_x_frame_options_deny(self):
        """X_FRAME_OPTIONS должен быть 'DENY'"""
        self.assertEqual(
            getattr(settings, 'X_FRAME_OPTIONS', ''),
            'DENY',
            "X_FRAME_OPTIONS должен быть 'DENY'"
        )

    def test_secure_browser_xss_filter(self):
        """SECURE_BROWSER_XSS_FILTER должен быть True"""
        self.assertTrue(
            getattr(settings, 'SECURE_BROWSER_XSS_FILTER', False),
            "SECURE_BROWSER_XSS_FILTER должен быть True"
        )

    def test_secure_content_type_nosniff(self):
        """SECURE_CONTENT_TYPE_NOSNIFF должен быть True"""
        self.assertTrue(
            getattr(settings, 'SECURE_CONTENT_TYPE_NOSNIFF', False),
            "SECURE_CONTENT_TYPE_NOSNIFF должен быть True"
        )


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)
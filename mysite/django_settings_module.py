# Установка переменной среды DJANGO_SETTINGS_MODULE, чтобы Django знал,
# где искать файл настроек проекта settings.py
# Для установки нужно ввести в Python консоли import django_settings_module
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

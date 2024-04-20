import os
from celery import Celery
from django.conf import settings

# Устанавливаем переменную окружения с названием проекта Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoinHub.settings')

# Создаем экземпляр приложения Celery
app = Celery('CoinHub')

# Загружаем настройки Celery из файла настроек Django
app.config_from_object('django.conf:settings')

# Автоматически регистрируем задачи из всех модулей "tasks.py" в приложениях Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

import os
from celery import Celery

# Устанавливаем переменную окружения 'DJANGO_SETTINGS_MODULE'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'C.settings')

# Создаем экземпляр приложения Celery
app = Celery('ваш_проект')

# Загружаем настройки Celery из файла settings.py проекта
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически определяем и загружаем задачи из всех модулей Django приложений в проекте
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

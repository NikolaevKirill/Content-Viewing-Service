"""
WSGI config for ContentViewingService project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import csv
from django.core.wsgi import get_wsgi_application
from search.models import Images


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ContentViewingService.settings")

application = get_wsgi_application()

# Очищаем базу данных при запуске сервера
Images.objects.all().delete()

# Загружаем файл конфигурации в базу данных
with open("static/configurations.csv", encoding="utf8") as file:
    reader = csv.reader(file)
    for line in reader:
        line = line[0].split(";")
        images = Images(url=line[0], number_of_show=line[1], categories=line[2:])
        images.save()

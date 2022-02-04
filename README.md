# Сервис просмотра контента
Текст задания расположен в файле `Задание.docx`

Запуск:

```shell
source myenv/bin/activate
pip install -r requirements.txt
python ContentViewingService/manage.py makemigrations
python ContentViewingService/manage.py migrate
python ContentViewingService/manage.py runserver 
```

Сервис будет доступен на `http://127.0.0.1:8000/`

Тестовый файл с конфигурацией `configurations.csv` находится в папке `ContentViewingService/static/`. Тестовые 
изображения расположены в той же папке.

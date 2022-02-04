# Сервис просмотра контента
Текст задания расположен в файле `Задание.docx`

Запуск:
1. cd in to the directory where you want your project to store you source code eg. home/ 
2. run `django-admin startproject ContentViewingService`
3. This will create a ContentViewingService directory in your current directory
4. Now cd to the ContentViewingService directory.
5. run `virtualenv env`
6. This will create a directory namely env. Now just activate the virtualenv by running `source /env/bin/activate` (if you are in the ContentViewingService dir).
7. Next:
```shell
python setup.py install
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

Сервис будет доступен на `http://127.0.0.1:8000/`

Тестовый файл с конфигурацией `configurations.csv` находится в папке `ContentViewingService/static/`. Тестовые 
изображения расположены в той же папке.

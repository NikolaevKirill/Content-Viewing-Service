# Сервис просмотра контента
Текст задания расположен в файле `Задание.docx`

Запуск на Windows:
```shell
cd Content-Viewing-Service
python -m venv venv
virtualenv --system-site-packages -p python ./venv
python setup.py install
pip install -r requirements.txt
cd ContentViewingService
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

Запуск на Linux:
```shell
cd Content-Viewing-Service
python3 -m venv venv
source venv/bin/activate
python setup.py install
pip install -r requirements.txt
cd ContentViewingService
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

Сервис будет доступен на `http://127.0.0.1:8000/`

Тестовый файл с конфигурацией `configurations.csv` находится в папке `ContentViewingService/static/`. Тестовые 
изображения расположены в той же папке.

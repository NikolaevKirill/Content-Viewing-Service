from django.shortcuts import render
from .models import Images
import csv
import random


def index(request):

    # Если база данных пустая, значит, мы запустили сайт, поэтому загрузим файл конфигурации
    if len(Images.objects.all()) == 0:
        with open("static/configurations.csv") as f:
            reader = csv.reader(f)
            for line in reader:
                line = line[0].split(";")
                images = Images(URL=line[0], NumberOfShows=line[1], categories=line[2:])
                images.save()

    return render(request, "search/index.html")


def show_picture(request):

    categories = request.GET.getlist("category")
    # Считываем категории в список, удаляем пустые категории
    indices = []  # Список с индексами незаполненных категорий

    for i, category in enumerate(categories):
        if category == " " or category == "":
            indices.append(i)

    k = 0  # Количество удалённых пустых категорий
    for i in indices:
        del categories[i - k]
        k += 1

    # Если запроса нет возвращаем случайное изображение
    if len(categories) == 0:
        ids = [elem["id"] for elem in Images.objects.values("id")]
        index_of_choose = random.choice(ids)

        # Обновление NumberOfShows
        picture = Images.objects.get(id=index_of_choose)
        picture.NumberOfShows -= 1
        picture.save()

        url = Images.objects.get(id=index_of_choose)
        return render(request, "search/show_picture.html", context={"URL": url})

    cross_indices = cross_categories(categories)
    if len(cross_indices) == 0:
        return render(request, "search/fail_response.html")

    index_picture = random.choice(cross_indices)
    id_picture = Images.objects.values("id")[index_picture]["id"]

    # Обновление NumberOfShows
    picture = Images.objects.get(id=id_picture)
    picture.NumberOfShows -= 1
    picture.save()
    url = Images.objects.get(id=id_picture)  # URL picture

    return render(request, "search/show_picture.html", context={"URL": url})


def cross_categories(search_categories):
    # Возвращает список индексов изображений (не id, а индексы), похожих категориями на запрос
    search_categories = set(search_categories)
    cross = []

    # Пересечения категорий
    for elem in Images.objects.values("categories"):
        categories = set(elem["categories"].split("'")[1::2])
        cross.append(len(categories & search_categories))

    # Возвращаем индексы только похожих на запрос изображений
    indices = [i for i in range(len(cross))]
    return [ind for i, ind in enumerate(indices) if cross[i] != 0]


def delete_db(request):
    #  При выходе очищаем базу данных
    Images.objects.all().delete()

    return render(request, "search/ThankYou.html")

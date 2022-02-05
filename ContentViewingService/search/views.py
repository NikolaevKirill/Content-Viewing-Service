import random
from django.shortcuts import render, HttpResponse
from .models import Images


def get_categories(request):
    """
    Функция принимает HTTP GET запрос и возвращает категории запрашиваемого изображения
    :param request: HTTP GET запрос
    :return: list, список с категориями
    """
    category = request.GET.getlist("category")
    # Если не одна категория, то категории выделаются по "category[]"
    if len(category) == 0:
        categories = request.GET.getlist("category[]")
        return categories
    else:
        return category


def cross_categories(search_categories):
    """
    Функция определяет пересечения категорий запроса и изображений и возвращает
    id пересекаемых изображений
    :param search_categories: list, содержит категории запроса
    :return: list, с индексами (не id), соответствующими изображениям в Images.objects.values
    :return: list, содержит словари dict{'id':id} изображений, подходящих запросу
    """

    search_categories = set(search_categories)
    cross = []

    # Пересечения категорий
    for elem in Images.objects.values("categories"):
        categories = set(elem["categories"].split("'")[1::2])
        cross.append(len(categories & search_categories))

    # Возвращаем id только похожих на запрос изображений
    ids = Images.objects.values("id")
    cross_inds = [i for i in range(len(cross)) if cross[i] != 0]
    return cross_inds, [ids[ind] for ind in cross_inds]


def val_ids(challenger_ids, indices=None):
    """
    Функция принимает список с dict{'id':id} и список с индексами этих id в Images.objects.values
    и возвращает список id изображений,которые необходимо показать
    :param challenger_ids: список с dict{'id':id}
    :param indices: list, список с индексами (не id),
    :return: list, список id изображений
    """

    number_of_show = [
        elem["number_of_show"] for elem in Images.objects.values("number_of_show")
    ]
    if indices is None:
        valid_ids = [
            elem["id"]
            for i, elem in enumerate(challenger_ids)
            if number_of_show[i] != 0
        ]
    else:
        valid_ids = [
            elem["id"]
            for i, elem in enumerate(challenger_ids)
            if number_of_show[indices[i]] != 0
        ]
    return valid_ids


def choose_url(valid_ids):
    """
    Функция принимает id соответствующих запросу изображений и возвращает url изображения для показа.
    Также уменьшает у выбранного изображения на единицу количество раз необходимых к показу
    :param valid_ids: list, список id соответствующих запросу изображений
    :return: str, url выбранного изображения
    """
    id_picture = random.choice(valid_ids)

    # Обновление number_of_show
    picture = Images.objects.get(id=id_picture)
    picture.number_of_show -= 1
    picture.save()

    url = Images.objects.get(id=id_picture)
    return url


def choose_picture(categories):
    """
    Функция принимает запрашиваемые категории и возвращает url случайного изображения
    в случае наличия подходящего изображения, None в случае отсутствия подходящего изображения
    :param categories: list, запрашиваеме категории
    :return: str, url изображения или None
    """
    # Если запроса нет, возвращаем случайное изображение
    if len(categories) == 0:

        valid_ids = val_ids(Images.objects.values("id"))
        if len(valid_ids) != 0:
            url = choose_url(valid_ids)
            return url
        else:
            return None
    # Если запрос есть, ищем подходящее изображение
    else:
        cross_inds, cross_ids = cross_categories(categories)
        if len(cross_ids) != 0:
            valid_ids = val_ids(cross_ids, indices=cross_inds)
            if len(valid_ids) != 0:
                url = choose_url(valid_ids)
                return url
            else:
                return None
        else:
            return None


def index(request):
    """
    Функция вызывает шаблон главной страницы при наличии подходящего изображения или
    выдает сообщение об отсутствии подходящего контента.
    """
    categories = get_categories(request)
    url = choose_picture(categories)

    if url is None:
        return HttpResponse("204")
    else:
        return render(request, "search/index.html", {"url": url})

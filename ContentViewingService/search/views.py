from django.shortcuts import render, HttpResponse
from . import utils


def index(request):
    """
    Функция вызывает шаблон главной страницы при наличии подходящего изображения или
    выдает сообщение об отсутствии подходящего контента.
    """
    categories = utils.get_categories(request)
    url = utils.choose_picture(categories)

    if url is None:
        return HttpResponse("204")
    else:
        return render(request, "search/index.html", {"url": url})

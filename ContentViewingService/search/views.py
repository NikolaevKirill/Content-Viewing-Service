from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'search/index.html')


def show_picture(request):
    categories = request.GET.getlist('category')
    print(categories)
    indices = []  # Список с индексами незаполненных категорий

    for i, category in enumerate(categories):
        if category == ' ' or category == '':
            indices.append(i)

    k = 0 # Количество удалённых пустых категорий
    for i in indices:
        del categories[i-k]
        k += 1

    out = "<h2>Categories: {0}</h2>".format(categories)
    return HttpResponse(out)

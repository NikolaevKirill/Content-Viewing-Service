from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('picture', views.show_picture, name='show_picture')
]

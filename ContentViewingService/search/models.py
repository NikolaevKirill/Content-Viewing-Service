from django.db import models


class Images(models.Model):
    URL = models.CharField('URL')
    NumberOfShows = models.IntegerField('NumberOfShows')
    categories = models.CharField('Categories')

    def __str__(self):
        return self.URL

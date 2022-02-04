from django.db import models


class Images(models.Model):
    URL = models.CharField("URL", max_length=250)
    NumberOfShows = models.IntegerField("NumberOfShows")
    categories = models.CharField("Categories", max_length=250)

    def __str__(self):
        return self.URL

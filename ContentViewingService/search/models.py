from django.db import models


class Images(models.Model):
    url = models.CharField("url", max_length=250)
    number_of_show = models.IntegerField("number_of_show")
    categories = models.CharField("categories", max_length=250)

    def __str__(self):
        return self.url

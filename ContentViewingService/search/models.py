from django.db import models


class Images(models.Model):
    url = models.CharField("url", max_length=250, default = None)
    number_of_show = models.IntegerField("number_of_show", default = 0)
    categories = models.CharField("categories", max_length=250, default = None)

    def __str__(self):
        return self.url

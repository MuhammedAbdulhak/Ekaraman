from django.db import models


# Create your models here.

class CanlıTv(models.Model):
    TvURL = models.URLField()

    class Meta:
        verbose_name_plural = "Canlı Tv"

from django.db import models

# Create your models here.
from grenade_type_app.models import GrenadeType
from maps_app.models import Map


class Grenade(models.Model):
    type = models.ForeignKey(GrenadeType, on_delete=models.CASCADE)
    tg_link = models.TextField(blank=False, null=False)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tg_link}'

    class Meta:
        verbose_name = 'Граната'
        verbose_name_plural = 'Гранаты'

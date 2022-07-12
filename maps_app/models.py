from django.db import models
from django.urls import reverse


class Map(models.Model):
    title = models.CharField(max_length=256, unique=True, blank=False, null=False)
    image = models.ImageField(blank=True, null=False)
    pos_name = models.ImageField(blank=True, null=False)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return f'{self.id}.{self.title}'

    def get_absolute_url(self):
        return reverse('map', kwargs={'pk': self.pk})

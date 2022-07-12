from django.db import models

# Create your models here.


class GrenadeType(models.Model):
    type = models.CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name = 'Тип гранаты'
        verbose_name_plural = 'Типы гранат'

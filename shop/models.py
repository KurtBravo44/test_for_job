from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class MenuItem(models.Model):
    """ Модель для меню дерева """

    name = models.CharField(max_length=200, verbose_name='Название')
    url = models.CharField(max_length=200, **NULLABLE, verbose_name='Ссылка')
    named_url = models.CharField(max_length=200, **NULLABLE, verbose_name='Именная ссылка')
    parent = models.ForeignKey('self', **NULLABLE, related_name='children', on_delete=models.CASCADE,
                               verbose_name='Родительский пункт')
    menu_name = models.CharField(max_length=200, verbose_name='Название меню')

    def get_url(self):
        if self.url:
            return self.url

        elif self.named_url:
            return reverse(self.named_url)

        return '#'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

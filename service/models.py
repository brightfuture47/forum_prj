from django.db import models

class Post(models.Model):

    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

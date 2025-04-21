from django.db import models

class News(models.Model):
    image = models.ImageField('Изоброжение', null=True, blank=True)
    title = models.CharField('Название статьи', max_length=255, null=True, blank=True)
    subtitle = models.TextField('Статья', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
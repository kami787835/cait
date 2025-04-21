from django.db import models
class Slider(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True, blank=True)
    img = models.ImageField('Изображение', null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=False)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Direction(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True)
    title = models.CharField('Направление', max_length=55, null=True, blank=True)

    class Meta:
        verbose_name = 'Направление Института'
        verbose_name_plural = 'Направление Института'

    def __str__(self):
        return self.title

class Laboratory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    activity = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Laboratory"

    class Meta:
        verbose_name = 'Laboratory'
        verbose_name_plural = 'Laboratories'

class Base(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    activity = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Base"

    class Meta:
        verbose_name = ' Base'
        verbose_name_plural = 'Bases'

class Gallery(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True)
    year = models.IntegerField(
        default=2000,
        choices=[(year, year) for year in range(2000, 3000)],
        verbose_name="Год фотографии",
    )

    def __str__(self):
        return f'{self.year}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерии'
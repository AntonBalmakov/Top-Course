from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    language = models.CharField(max_length=30, db_index=True, verbose_name='Язык')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Изменено')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    requirement = models.TextField(null=True, blank=True, verbose_name='Требование к курсу')
    sale = models.IntegerField(default=0, verbose_name='Скидка в %')
    videos = models.ForeignKey('Video', null=True, on_delete=models.PROTECT, verbose_name='Видео')
    feedback = models.ForeignKey('Feedback', null=True, on_delete=models.PROTECT, verbose_name='Отзывы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['feedback__rate']


class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    order_number = models.IntegerField(verbose_name='Порядковый номер')
    link = models.TextField(verbose_name='Название')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'
        ordering = ['order_number']


class Feedback(models.Model):
    content = models.TextField(verbose_name='Описание')
    rate = models.IntegerField(verbose_name='Оценка')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-published']

from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    short_description = models.CharField('Краткое описание фильма', max_length=200)
    text = models.TextField('Ваше мнение о фильме')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
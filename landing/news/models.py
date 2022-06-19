from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    # blank - необязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # auto_now_add - заполняет время создания авто
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # - время эдита
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # - есть еще filefield, там можно грузить все файлы
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    
    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'news_id': self.pk})
    
    def myfunc(self):
        return('Hello from model!')
    
    def __str__(self):
        return self.title
    
    # ^ - это строковое представление объектов
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
        
        
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    # db.index - индексирует поле, что делает в дальнейшем более быстрый поиск по тайтлу
    
    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
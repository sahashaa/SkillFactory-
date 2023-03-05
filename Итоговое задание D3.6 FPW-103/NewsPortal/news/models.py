from django.db import models
from django.core.validators import MinValueValidator



# Товар для нашей витрины
class News(models.Model):#Создание модели новости
    Title = models.CharField(#Поле для Загловка
        max_length=50,
        unique=True, # Название новости должно быть уникальным
    )
    Text = models.TextField()#Поле для текста статьи
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все продукты в категории будут доступны через поле news
    )
    pub_time = models.DateTimeField(auto_now_add=True)#Поле для указания даты создания новсти

    def __str__(self):
        return f'{self.Title.title()}: {self.Text[:20]}'


# Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()




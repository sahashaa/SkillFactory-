from django.db import models#Импорт моделей
from django.contrib.auth.models import User#Импорт стандартной модели юзер
from django.db.models import Sum #Импорт функции сум


class Author(models.Model): #Создание модели "Автор"
    Auser = models.OneToOneField(User, on_delete=models.CASCADE) #Связь один ко одному с импортированной моделью юзер

    AuthorName = models.CharField(max_length=16, default="noname") #Поле имени Автора

    Arating = models.IntegerField(default=0) #Поле Рэейтинга автора

    def Like(self): #Метод лайк,просто увеличивает рейтинг,через сумму к полю Arating
        self.Arating += 1
        self.save()

    def Dislike(self): #Метод дизлайк,просто уменьшает рейтинг через вычитаение от поля Arating
        self.Arating -= 1
        self.save()

    def update_rating(self): #Метод обновления рэейтинга
        postRat = self.Post_set.aggregate(postRating=Sum('Prating')) #Сбор всех полей Prating со всех постов связанных с автором
        Prat = 0
        Prat += postRat.get("postRating")

        comentRat = self.Auser.Comment_set.aggregate(comRating=Sum('Crating')) #Сбор всех полей Сrating со всех коментариев связанных с автором
        Crat = 0
        Crat += comentRat.get('comRating')

        self.ratingAuthor = Prat * 3 + Crat #Сложение Агрегированных рейтингов от связанных коментариев и связанных постов
        self.save()


class Category(models.Model): #Модель категории
    it = 'IT'
    sport = 'SP'
    beauty = 'BT'
    casual = 'CS'

    CHOICE_CATEGORY = [
        (it, 'АйТи'),
        (sport, 'Спорт'),
        (beauty, 'Красота'),
        (casual, 'Повседневность')]

    category = models.CharField(max_length=2, choices=CHOICE_CATEGORY, default=casual, unique=True)#Поле "стандартных" категорий
    subcategory = models.CharField(max_length=128,unique=True)#Поле "произвольных" категорий

class Post(models.Model):#Модель постов
    News = 'NW'
    Article = 'AC'
    CHOISE_POST = [                                   #Создание типов  "Шаблонов",для постов
        (News, 'Новость'),
        (Article, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)#Связь один ко многим,пост-"зависимая" Автор-"главная"

    Cpost = models.CharField(max_length=2, choices=CHOISE_POST, default=Article)#Тип поста

    Time_add = models.DateTimeField(auto_now_add=True)#Поле добовляющее дату создания поста

    postCategory = models.ManyToManyField(Category, through='PostCategory')#Связь многие ко многим с промежуточной таблицей для последущей свзяи с моделью категорий

    Title = models.CharField(max_length=128)#Поле загаловка ,поста

    Text = models.TextField()#Поле текста,поста

    Prating = models.IntegerField(default=0)#Рэйтинг Поста

    def Like(self):#Метод лайк,просто увеличивает рейтинг,через сумму к полю Prating
        self.Prating += 1
        self.save()

    def Dislike(self):#Метод дизлайк,просто уменьшает рейтинг,через вычитание  от поля Prating
        self.Prating -= 1
        self.save()

    def preview(self):#Метод preview,через ф строки достает из поля Text первые 123 символа добовляет ... а также рейтинг поста
        return f'{self.Text[0:123]} ... {self.Prating}'


class PostCategory(models.Model):#Модель категорий для  постов
    postThrough= models.ForeignKey(Post, on_delete=models.CASCADE)#Промяжуточная свзь,для связи категорий и поста(Одни ко многим),PC-"Второстепенная",Post-основная

    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)#Связь между Category и PostCategory для последущей связи с моделью Post(Один ко многим)PC- "Второстепенная" Category-Основная


class Comment(models.Model):#Модель Коментариев
    CommentPost = models.ForeignKey(Post, on_delete=models.CASCADE)#Связь с моделью Post,Один ко многим,Пост-главная,Комент -второстепенная
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)#Связь с моделью юезр,Один ко многим Юзер-главная,Комент второстепенная

    Text = models.TextField(max_length=256)#Поле текста сообщения самого коментария

    Time_add = models.DateTimeField(auto_now_add=True)#Поле добавляющее время создания коментария

    Crating = models.IntegerField(default=0)#Рейтинг коментария

    def Like(self):
        self.Crating += 1
        self.save()

    def Dislike(self):
        self.Crating -= 1
        self.save()

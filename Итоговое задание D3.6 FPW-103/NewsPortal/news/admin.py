from django.contrib import admin
from .models import Category, News


admin.site.register(Category)#Регистрация в админ панели графы категории
admin.site.register(News)#Регистрации графы News


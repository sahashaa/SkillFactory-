from django import template

register = template.Library()

@register.filter()
def cenzor(value):
    # Список нежелательных слов
    forbidden_words = ['bad', 'evil', 'spam','Редиска']

    # Заменяем буквы нежелательных слов на символ '*'
    for word in forbidden_words:
        value = value.replace(word, '*' * len(word))

    return value

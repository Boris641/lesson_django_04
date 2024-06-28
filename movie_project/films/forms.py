from . models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForms(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description':  TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше мнение о фильме'}),
            ' pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),

        }
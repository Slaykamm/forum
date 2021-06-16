from django.db.models.fields import CharField
from django_filters import FilterSet
from django_filters.filters import ChoiceFilter  # импортируем filterset,
from .models import Comment , Post
from django.forms.widgets import ChoiceWidget, SelectDateWidget, TextInput, Textarea
from django.forms import widgets
from django_filters import CharFilter 

 
 
# создаём фильтр
class PostFilter(FilterSet):

    post_title=CharFilter(field_name='post_title', lookup_expr='icontains', label="", widget=TextInput(attrs=
            {'placeholder': 'Искать по заглавию сообщения', 
            'class': 'form-control',
            'size': 10, }))





    class Meta:
        model = Post
        #fields = ('post_title', 'post_date', 'author_post', 'category_post')  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
        #    'post_title': ['icontains'],  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author_post',  # количество товаров должно быть больше или равно тому, что указал пользователь
            'category_post',  # цена должна быть меньше или равна тому, что указал пользователь
        }
        exclude=['post_title']



class CommentFilter(FilterSet):
    class Meta:
        model = Comment
#        fields = ('author_comment',)
        fields = {
            'comment_date' ,
            'comment_post' ,
            'comment_text' ,  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author_comment' ,  # количество товаров должно быть больше или равно тому, что указал пользователь
        }

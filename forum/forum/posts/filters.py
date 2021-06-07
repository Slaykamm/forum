from django_filters import FilterSet  # импортируем filterset,
from .models import Post

 
 
# создаём фильтр
class PostFilter(FilterSet):
    class Meta:
        model = Post
        #fields = ('post_title', 'post_date', 'author_post', 'category_post')  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
            'post_title': ['icontains'],  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author_post': ['in'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'category_post': ['in'],  # цена должна быть меньше или равна тому, что указал пользователь
        }


from django.urls import path
from .views import PostsList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, PostSearch
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'), 
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create_comment/<int:pk>', CommentCreateView.as_view(), name='create_comment'),
    path('search/', PostSearch.as_view(), name='post_search'),
      
]   
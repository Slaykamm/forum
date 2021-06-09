from django.urls import path
from .views import PostsList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, PostSearch, ContactDetailView, CommentUpdateView, CommentDeleteView

 
urlpatterns = [

    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'), 
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create_comment/<int:pk>', CommentCreateView.as_view(), name='create_comment'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('contact/', ContactDetailView.as_view(), name='forum_contact'),
    path('update_comment/<int:pk>', CommentUpdateView.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
      
]   
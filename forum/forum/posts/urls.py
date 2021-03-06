from django.urls import path
from .views import PostsList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, PostSearch, ContactDetailView,  CommentDeleteView, CommentDetailView, CommentUpdateView, CommentFeedbackView, PostDetailFromComments


 
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
    path('feedback_comment/<int:pk>', CommentFeedbackView.as_view(), name='feedback_comment'), 
    path('delete_comment/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
    path('comment_list', CommentDetailView.as_view()),
    path('post/<int:pk>', PostDetailFromComments.as_view(), name='post_detail_from_comment'),
    


      
]   
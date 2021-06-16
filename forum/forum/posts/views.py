from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  
from .models import Category, Post, Comment, Author
from .filters import CommentFilter,  PostFilter 
from .forms import PostForm, CommentForm
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.paginator import Paginator  

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html

from django.views.generic.base import RedirectView
from django.urls import reverse


from .tasks import weeklyUpdates

  
 
class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, 
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by = 3 

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        #context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст

        weeklyUpdates()

        if self.request.user.is_authenticated: 
            author = Author.objects.filter(author_user = self.request.user).exists() #делаем всех авторами, как просят в ТЗ
            if not author:
                Author.objects.create(author_user=self.request.user)
        return context





@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        id = self.kwargs.get('pk')
        post_comments = Comment.objects.filter(comment_post = Post.objects.get(id = id))
        context['comments'] = post_comments  

        author_flag = False   #это и ниже это чтбы кнопки редактировать и удалять горели только у автора сообщения
        com_author = Post.objects.get(id = id).author_post
        actual_user = self.request.user       
        if str(com_author) == str(actual_user):
            author_flag = True
        context['author_flag'] = author_flag

        return context

@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного

        return context

    def get_object(self, **kwargs):

        return    Post.objects.create(author_post =  Author.objects.get(author_user = self.request.user))

 

@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context


@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentCreateView(UpdateView):
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context


    def get_object(self, **kwargs):
        
        id = self.kwargs.get('pk')

        return Comment.objects.create(comment_post = Post.objects.get(id = id), author_comment = Author.objects.get(author_user = self.request.user))


@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentUpdateView(UpdateView):
    template_name = 'comment_create.html'
    form_class = CommentForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')

        return Comment.objects.get(pk=id)

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        com_author = Comment.objects.get(id = id).author_comment
        actual_user = self.request.user
        print(str(com_author), str(actual_user))
        if str(com_author) != str(actual_user):
            return HttpResponseForbidden()
        return super().form_valid(form)



        
@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Comment.objects.all()
    success_url = '/comment_list'



 
class PostSearch(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'post_search.html'  # указываем имя шаблона, в котором будет лежать HTML, 
                                    #в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by = 5 

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context



class ContactDetailView(ListView):
    model = Post
    template_name = 'forum_contact.html'
    context_object_name = 'post'
    queryset = Post.objects.all()  



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context



#обрабатываем страницу с комментариями автора.
@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentDetailView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'author_comment_context'
    queryset = Comment.objects.order_by('-comment_date')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        id = self.kwargs.get('pk')
        userAuthorCheck = Author.objects.filter(author_user = self.request.user).exists()
        if userAuthorCheck:    # работает только если юзер писатель, иначе не возращает ничего
            post_author = Post.objects.filter(author_post = Author.objects.get(author_user = self.request.user))
            post_comments = Comment.objects.filter(comment_post__author_post = Author.objects.get(author_user = self.request.user))
            for post in post_comments:
                if len(str(post.comment_text)) == 0:
                    empty = Comment.objects.get(id = post.id)
                    empty.delete()

            context['comments'] = post_comments  
            context['filter'] = CommentFilter(self.request.GET, queryset=post_comments)   #self.get_queryset()) 
            context['post'] = Post.objects.all()

        return context



@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentFeedbackView(DetailView):
    
    model = Comment
    template_name = 'comment_list.html'  
    context_object_name = 'feedback_comment'
    queryset = Comment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['logged_user'] = self.request.user.username
        post_comments = Comment.objects.filter(comment_post__author_post = Author.objects.get(author_user = self.request.user))
        context['comments'] = post_comments  
        context['filter'] = CommentFilter(self.request.GET, queryset=post_comments)
        feedback_comment_author = Comment.objects.get(id = id).author_comment
        feedback_comment_text = Comment.objects.get(id = id).comment_text
        feedback_comment_author_email = User.objects.get(username=str(feedback_comment_author)).email
        post_id = Comment.objects.get(id = id).comment_post.id 
        post_commented_title = Post.objects.get(id=post_id).post_title


        emails_list = [] 
        emails_list.append(feedback_comment_author_email)

        #if feedback_comment_author_email:
        html_content = render_to_string( 
        'email_comment_feedback.html',
        {
        'feedback_comment_author': feedback_comment_author, 
        'feedback_comment_text': feedback_comment_text, 
        'post_commented_title': post_commented_title, 
        'id': post_id,
        
        }

        )

        msg = EmailMultiAlternatives(
        subject=f'Благодарим за комментарий ',   
        
        body=f'Благодарим за комментарий ', 
        from_email= 'destpoch77@mail.ru', #'destpoch22@mail.ru',  #'destpoch22@mail.ru'
        to=  emails_list
        )

        msg.attach_alternative(html_content, "text/html")
        
        print("вместо отправки извещения на изменение печатаем",  feedback_comment_author, feedback_comment_text, post_commented_title, post_id  )
        msg.send() # отсылаем


        return context


#это мы делаем переадресацию чтобы кликал в однйо модели, брал аргумент и тащил в другую модель.

class PostDetailFromComments(RedirectView):

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()  
    
    def get_redirect_url(self, pk):
        post_comments_id = Comment.objects.get(id = pk).comment_post.id 
        return reverse('post_detail', args=(post_comments_id,))


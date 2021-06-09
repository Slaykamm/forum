from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  
from .models import Category, Post, Comment, Author
from .filters import PostFilter  
from .forms import PostForm, CommentForm
#from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
  
 
class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, 
                                    #в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
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
        return context

@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context


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
        print('id', id, Comment.objects.get(pk=id))
        return Comment.objects.get(pk=id)

        
@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class CommentDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Comment.objects.all()
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context






 
class PostSearch(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'post_search.html'  # указываем имя шаблона, в котором будет лежать HTML, 
                                    #в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')

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
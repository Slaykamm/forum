from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  
from .models import Category, Post, Comment
from .filters import PostFilter  
from .forms import PostForm, CommentForm
  
 
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


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context


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

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context

class CommentCreateView(UpdateView):
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного
        return context


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Comment.objects.create(comment_post = Post.objects.get(id = id))
        

 
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
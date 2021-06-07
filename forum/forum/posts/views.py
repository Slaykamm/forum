from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  
from .models import Post, Comment


from .filters import PostFilter  
from .forms import PostForm
  
 
class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, 
                                    #в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        print(id)
        post_data = Post.objects.get(id = id)
        postCat = Post.objects.get(pk=id)
        post_comments = Comment.objects.filter(comment_post = Post.objects.get(id = id))
        
        comments = Comment.objects.all()
        context['comments'] = post_comments  

        return context


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
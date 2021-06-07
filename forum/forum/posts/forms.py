from django.forms import ModelForm, Textarea

from .models import Post
 
 
class PostForm(ModelForm):

 
    class Meta:
        model = Post
        fields = ['post_title',  'post_text',  'author_post', 'category_post' ]  # н странице!
        widgets = {
            'post_title': Textarea(attrs={'cols': 80, 'rows': 1}),
            'post_text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


    
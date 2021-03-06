from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField




class Author(models.Model):
    author_user  = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    title_category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.title_category}'


class Post(models.Model):
    post_title = models.CharField(max_length = 64, default = "Your message")
    post_date = models.DateField(auto_now_add = True)
    #post_text = models.TextField(default='')
    post_text = RichTextField(blank = True, null = True)
    post_rating = models.IntegerField(default = 0)

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_post = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.post_title}'





    def get_absolute_url(self): 
        return f'/posts/{self.id}' 



class Comment(models.Model):
    title_comment = models.CharField(max_length=64, blank=True, default='')
    comment_text = models.TextField(default='')
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, default='2')
    comment_date = models.DateField(auto_now_add = True)
    author_comment = models.ForeignKey(Author, on_delete=models.CASCADE, default='1')     

    def __str__(self):
        return f'{self.comment_text}'

    def get_absolute_url(self): 
        return f'/posts/{self.comment_post_id}'




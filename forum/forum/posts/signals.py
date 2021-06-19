from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string
from .models import Post, Comment, User
#from django.db.models.signals import post_save
from django.dispatch import receiver


#@receiver(post_save, sender=Comment)  #

def notify_post_athour_comment(sender, instance,  **kwargs): #created,
    id = instance.id   # получаем ID побуликованной сообщения
    test_create = Comment.objects.get(id = id).comment_text
   
    if len(test_create) > 0:
        post_comments_id = Comment.objects.get(id = id).comment_post.id  #получили ай ди новости к которой комментарий
        post_title = Comment.objects.get(id = id).comment_post.post_title
        post_author = Comment.objects.get(id = id).comment_post.author_post   #имя автора поста
        post_author_email = User.objects.get(username=str(post_author)).email    #и его емаил
        emails_list = [] 
        emails_list.append(post_author_email)

        if post_author_email:
            html_content = render_to_string( 
            'email_comment_created.html',
            {
            'post_author': post_author, 'post_comments_author': instance.author_comment, 'post_title':post_title, 'id' : post_comments_id,
            }

            )

            msg = EmailMultiAlternatives(
            subject=f'Комментарий на Ваш пост ',   
                    
            body=f'Комментарий на Ваш пост', 
            from_email= 'destpoch77@mail.ru', #'destpoch22@mail.ru',  #'destpoch22@mail.ru'
            to=  emails_list
            )

            msg.attach_alternative(html_content, "text/html")
            print("вместо отправки извещения на изменение печатаем",  'post_author', post_author, 'post_comments_author', instance.author_comment, 'post_title', post_title, 'ID', post_comments_id )
            #msg.send() # отсылаем






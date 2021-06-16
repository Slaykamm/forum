from celery import shared_task
from datetime import datetime, timedelta
from .models import Post, User

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string


@shared_task

def weeklyUpdates():
    freshPosts = Post.objects.values_list('id', flat=True).exclude(post_date__lt = datetime.now()-timedelta(days=7))   #получаем все новости за неделю

    freshPostsIds = []

    for idk in freshPosts:
        freshPostsIds.append(idk)  # тут получил список айти новостей за неделю из Queryset

    userList = User.objects.all()

    for userinfo in userList:
        userEmail = User.objects.get(username = str(userinfo)).email  # получили емаил

        if userEmail:
            # формируем список id для отправки

                

            
            html_content = render_to_string( 
            'subscribe_weekly.html',
            {
            'user': userinfo, 'art_id':freshPostsIds,
            }

            )
            msg = EmailMultiAlternatives(
            subject=f'{userinfo} ',    #кому
            
            body=f'недельные обновления на форуме', 
            from_email='destpoch77@mail.ru',
            to=[f'{userEmail}', ]  
            )

            msg.attach_alternative(html_content, "text/html")
            #print("Вместо отправки еженедельной подписки печатаем", 'user', userinfo, 'art_id',freshPostsIds)
            msg.send() # отсылаем



 
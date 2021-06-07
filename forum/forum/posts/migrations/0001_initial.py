# Generated by Django 3.2.4 on 2021-06-07 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_comment', models.CharField(default='', max_length=64)),
                ('comment_text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default='Your message', max_length=64)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_text', models.TextField(default='')),
                ('post_rating', models.IntegerField(default=0)),
                ('author_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.author')),
                ('category_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
            ],
        ),
    ]

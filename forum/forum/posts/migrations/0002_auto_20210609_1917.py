# Generated by Django 3.2.4 on 2021-06-09 19:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_comment',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='posts.author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title_comment',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
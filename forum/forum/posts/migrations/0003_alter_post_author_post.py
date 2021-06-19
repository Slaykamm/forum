# Generated by Django 3.2.4 on 2021-06-19 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210612_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_post',
            field=models.ForeignKey(default='User.username', on_delete=django.db.models.deletion.CASCADE, to='posts.author'),
        ),
    ]
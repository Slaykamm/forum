# Generated by Django 3.2.4 on 2021-06-07 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(default='5', on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title_comment',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
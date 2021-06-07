# Generated by Django 3.2.4 on 2021-06-05 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_category',
        ),
        migrations.AddField(
            model_name='comment',
            name='title_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.category'),
            preserve_default=False,
        ),
    ]
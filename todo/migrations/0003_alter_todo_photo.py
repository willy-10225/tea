# Generated by Django 4.0.6 on 2022-08-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Прочитано'),
        ),
    ]

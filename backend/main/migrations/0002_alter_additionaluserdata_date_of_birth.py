# Generated by Django 4.1.2 on 2022-10-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaluserdata',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
    ]
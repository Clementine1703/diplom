# Generated by Django 4.1.2 on 2022-10-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_additionaluserdata_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaluserdata',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
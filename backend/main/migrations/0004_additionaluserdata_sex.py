# Generated by Django 4.1.2 on 2022-10-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_additionaluserdata_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaluserdata',
            name='sex',
            field=models.CharField(blank=True, choices=[('ML', 'Male'), ('FL', 'Female')], max_length=2, null=True, verbose_name='Гендер'),
        ),
    ]
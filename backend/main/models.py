from django.db import models
from django.contrib.auth.models import User
import datetime


# Данные пользователей
class AdditionalUserData(models.Model):
    JUNIOR = 'JR'
    MIDDLE = 'ML'
    SENIOR = 'SR'
    EXPERIENCE_CHOICES = [
        (JUNIOR, 'Junior'),
        (MIDDLE, 'Middle'),
        (SENIOR, 'Senior'),
    ]
    MALE = 'ML'
    FEMALE = 'FL'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=60, verbose_name='Имя', blank=True)
    user_status = models.CharField(max_length=150, verbose_name='Статус', blank=True)
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения', blank=True)
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    experience = models.CharField(
        max_length=2,
        choices=EXPERIENCE_CHOICES,
        default=JUNIOR,
        verbose_name='Опыт',
        blank=True)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True, null=True, verbose_name='Гендер')

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = "Данные пользователей"

    def __str__(self):
        return 'Данные'


# Списки чатов
class Chat(models.Model):
    chat = models.AutoField(primary_key=True, verbose_name='id чата')
    name = models.CharField(max_length=50, verbose_name='Название чата')
    last_modified_date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Список чатов'
        verbose_name_plural = "Список чатов"

    def __str__(self):
        return self.name


# Списки участников чата
class ChatUser(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='id чата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя')

    class Meta:
        verbose_name = 'Участники чата'
        verbose_name_plural = "Участники чата"

    def __str__(self):
        return self.user.username


# Списки сообщений
class Message(models.Model):
    message_id = models.AutoField(primary_key=True, verbose_name='id сообщения')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='id чата')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='id пользователя')
    content = models.CharField(max_length=500, verbose_name='контент')
    date_create = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='дата создания')
    read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = 'Список сообщений'
        verbose_name_plural = "Список сообщений"

    def __str__(self):
        return self.chat.name


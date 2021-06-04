from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False, blank=True, null=True)
    email = models.EmailField(unique=True)
    patronymic = models.CharField(max_length=20, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic', 'username']

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.patronymic

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
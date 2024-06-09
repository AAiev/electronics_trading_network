from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'email: {self.email}'

    verbose_name = 'пользователь'
    verbose_name_plural = 'пользователи'

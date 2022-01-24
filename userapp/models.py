from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    is_partner = models.BooleanField(default=False, verbose_name='Пользователь-партнер', db_index=True)
    is_organization = models.BooleanField(default=False, verbose_name='Пользователь-организация', db_index=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.username}'

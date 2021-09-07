from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles:
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'user'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
    )


class User(AbstractUser):

    bio = models.CharField(
        max_length=4000,
        null=True,
        blank=True,
        verbose_name='Биография'
    )
    email = models.EmailField(
        unique=True,
        db_index=True,
        verbose_name='Почта',
    )
    role = models.CharField(
        max_length=30,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name='Роль'
    )

    @property
    def is_admin(self):
        return self.is_staff or self.role == Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR

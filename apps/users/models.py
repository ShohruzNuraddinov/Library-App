from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.choices import UserRole
from apps.users.managers import UserManager
# Create your models here.


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    first_name = None
    last_name = None
    username = None
    name = models.CharField(_("Name: "), max_length=255)
    email = models.EmailField(_("Email: "), unique=True)
    role = models.CharField(
        _("Role: "),
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER,
    )

    # Add any additional fields you want here
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.email

    @property
    def tokens(self):
        refresh_token = RefreshToken.for_user(self)
        return {
            "access": str(refresh_token.access_token),
            "refresh": str(refresh_token),
        }

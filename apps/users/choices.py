from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    """
    User roles for the application.
    """
    ADMIN = "admin", _("Admin")
    USER = "user", _("User")


__all__ = ["UserRole"]

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.common.models import BaseModel
# Create your models here.


class Genre(BaseModel):
    name = models.CharField(_("Name: "), max_length=255)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name


class Author(BaseModel):
    first_name = models.CharField(_("First Name: "), max_length=255)
    last_name = models.CharField(_("Last Name: "), max_length=255)
    birth_date = models.DateField(_("Birth Date: "), blank=True, null=True)
    death_date = models.DateField(_("Death Date: "), blank=True, null=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(BaseModel):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name="books")

    title = models.CharField(_("Title: "), max_length=255)
    description = models.TextField(_("Description: "), blank=True, null=True)
    length = models.PositiveIntegerField(_("Length: "), blank=True, null=True)
    published_date = models.DateField(
        _("Published Date: "), blank=True, null=True)
    created_date = models.DateField(_("Created Date: "), auto_now_add=True)
    copies_sold = models.PositiveIntegerField(_("Copies Sold: "), default=0)
    price = models.DecimalField(
        _("Price: "), max_digits=10, decimal_places=2
    )
    discount = models.IntegerField(_("Discount: "), default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100),
    ])
    cover = ResizedImageField(_("Cover: "), size=[
                              300, 400], upload_to="books/covers/", blank=True, null=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title


class Rating(BaseModel):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ratings")
    rate = models.DecimalField(
        _("rate: "),
        max_digits=2,
        decimal_places=1,
    )

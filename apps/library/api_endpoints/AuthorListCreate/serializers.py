from rest_framework import serializers

from apps.library.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='gender.name', read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "genre",
            "length",
            "published_date",
            "created_date",
            "copies_sold",
            "price",
            "discount",
            "cover"
        )


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
            "books",
        )


__all__ = ['AuthorSerializer']

from rest_framework import serializers

from apps.library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    """

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birth_date", "death_date",)
        read_only_fields = ("id",)


class BookCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a book.
    """
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=Author.objects.all(),
        write_only=True
    )
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "author_id",
            "author",
            "title",
            "description",
            "genre",
            "length",
            "published_date",
            "created_date",
            "copies_sold",
            "price",
            "discount",
            "cover",
        )
        read_only_fields = ("id",)


__all__ = ["BookCreateSerializer"]

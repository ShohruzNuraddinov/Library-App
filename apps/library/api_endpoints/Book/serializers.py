from rest_framework import serializers

from apps.library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birth_date", "death_date")
        read_only_fields = ("id",)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # For GET (output)
    author_id = serializers.PrimaryKeyRelatedField(  # For POST/PATCH (input)
        source="author",
        queryset=Author.objects.all(),
        write_only=True,
    )
    genre = serializers.CharField(source="genre.name")

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "length",
            "published_date",
            "created_date",
            "copies_sold",
            "price",
            "discount",
            "cover",
            "author",
            "author_id",
            "genre",
        )
        read_only_fields = ("id", "created_date")


__all__ = ["BookSerializer"]

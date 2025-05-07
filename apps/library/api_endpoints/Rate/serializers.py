from rest_framework import serializers

from apps.library.models import Rating


class RateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rate model.
    """

    class Meta:
        model = Rating
        fields = ("id", "rate", "user", "book")
        read_only_fields = ("id", "user", "book")


__all__ = ["RateSerializer"]

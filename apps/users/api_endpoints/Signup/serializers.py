from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer for user signup.
    """

    class Meta:
        model = User
        fields = ("email", "password", "name",)
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


__all__ = ["SignupSerializer"]
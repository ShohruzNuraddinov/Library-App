from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": _("User with this email does not exist.")})

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"password": _("Incorrect password.")})

        if not user.is_active:
            raise serializers.ValidationError(
                {"email": _("This account is inactive.")})

        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        return validated_data['user'].tokens


__all__ = ["LoginSerializer"]

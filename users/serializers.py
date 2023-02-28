from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer for Signup ViewSet
    """

    # We have to redeclare the password field and add a new field for
    # password confirm
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "confirm_password")

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Passwords fields did not match !"}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["email"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

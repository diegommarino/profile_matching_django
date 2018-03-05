from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class SigninSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    auth_token = serializers.ReadOnlyField()

    class Meta:
        model = get_user_model()
        fields = ('id',
                  'email',
                  'password',
                  'auth_token')

    def create(self, validated_data):
        user = super(SignupSerializer, self).create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value).last()
        if user:
            raise serializers.ValidationError("Email already registered.")
        return value

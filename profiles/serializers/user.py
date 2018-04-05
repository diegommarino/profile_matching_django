from rest_framework import serializers
from profile_matching.profiles.models.profile import Profile
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id',
                  'email',
                  'profile',
                  'password',
                  'is_staff',
                  'auth_token')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.get_or_create(user=user)
        return user

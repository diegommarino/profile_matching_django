from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from profiles.serializers.user import UserSerializer
from profiles.serializers.auth import SigninSerializer
from profiles.serializers.auth import SignupSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def logout(request):
    user = get_user_model().objects.filter(auth_token=request.data.get('auth_token')).last()
    user.auth_token.delete()
    return Response({}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    serialized = SignupSerializer(data=request.data)

    if serialized.is_valid():
        user = serialized.create(request.data)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_in(request):
    serialized = SigninSerializer(data=request.data)

    if serialized.is_valid():
        user = get_user_model().objects.filter(email=request.data.get('email')).first()
        if user and user.check_password(request.data.get('password')):
            create_or_retrieve_user_token(user)
        else:
            return Response(
                {'errors': 'Wrong auth data.'},
                status=status.HTTP_401_UNAUTHORIZED)

        user_serialized = UserSerializer(user)
        return Response(user_serialized.data, status=status.HTTP_200_OK)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


def create_or_retrieve_user_token(user):
    from rest_framework.authtoken.models import Token
    Token.objects.get_or_create(user=user)

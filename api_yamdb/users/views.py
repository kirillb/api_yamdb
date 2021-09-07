from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from users.permissions import IsAdmin
from users.serializers import (
    GenCodeSerializer,
    GenTokenSerializer,
    UserSerializer
)


code_generator = PasswordResetTokenGenerator()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdmin, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @action(
        detail=False,
        methods=('GET', 'PATCH'),
        permission_classes=(IsAuthenticated,),
        name='update_self'
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)

        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)

        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_confirmation_code(request):

    serializer = GenCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = request.data.get('email')
    username = request.data.get('username')

    if username == 'me':
        return Response(
            {'username': ['username "me" is not allowed']},
            status=status.HTTP_400_BAD_REQUEST
        )

    user, created = User.objects.get_or_create(
        email=email,
        username=username
    )

    if created:
        user.is_active = False
        user.save()

    confirmation_code = code_generator.make_token(user)

    send_mail(
        'Confirmation code - API tamdb',
        f'Confirmation code is {confirmation_code}',
        None,
        (email, )
    )

    return Response(
        {'email': email, 'username': username},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_auth_token(request):

    serializer = GenTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)

    confirmation_code = serializer.validated_data.get('confirmation_code')

    if not code_generator.check_token(user, confirmation_code):
        return Response(
            {'confirmation_code': ['Code is not recognized']},
            status=status.HTTP_400_BAD_REQUEST
        )

    user.is_active = True
    user.save()

    return Response({'token': str(AccessToken.for_user(user))})

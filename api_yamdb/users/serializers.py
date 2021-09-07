from users.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role'
        )
        model = User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=(UniqueValidator(queryset=User.objects.all()),)
    )
    email = serializers.EmailField(
        validators=(UniqueValidator(queryset=User.objects.all()),)
    )


class GenTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=128)

from django.contrib import auth
from rest_framework import serializers
# from django.contrib.auth import get_user_model, authenticate
# from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed

from .models import *

# UserModel = get_user_model()
#
#
# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = '__all__'
#     def create(self, clean_data):
#         user_obj = UserModel.objects.create_user(
#             name=clean_data['name'],
#             password=(clean_data['password']),
#             identification_type=clean_data['identification_type'],
#             identification_number=clean_data['identification_number'],
#             email=clean_data['email'],
#             phone_number=clean_data['phone_number']
#         )
#         user_obj.save()
#         return user_obj
#
#
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#
#     def check_user(self, clean_data):
#         user = authenticate(
#             username=clean_data['email'], password=clean_data['password'])
#         if not user:
#             raise ValidationError('User not found or incorrect password')
#         return user
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["user_id", "last_login", "name", "email", "identification_type", "identification_number", "phone_number", "updated_at"]


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=255, min_length=3, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disables, contact admin')

        return {
            'id': user.id,
            'email': user.email,
            'name': user.name,
        }
        return super(LoginSerializer, self).validate()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type'}, min_length=4, max_length=12, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user

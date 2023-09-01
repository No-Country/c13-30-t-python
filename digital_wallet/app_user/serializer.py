from rest_framework import serializers
from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['identification_number',
                  'phone_number'
                  ]


class CreateUserDetailSerializer(serializers.ModelSerializer):
    id_detail = UserDetailSerializer()

    class Meta:
        model = User
        fields = ['name',
                  'email',
                  'password',
                  'id_detail'
                  ]

    def create(self, validated_data):
        # Extrae los detalles del usuario
        id_detail_data = validated_data.pop('id_detail')
        # Crea el usuario con los datos validados
        user = User.objects.create(**validated_data)
        # Crea los detalles del usuario
        UserDetail.objects.create(user=user, **id_detail_data)
        return user

    # def to_representation(self, instance):
    #     return {
    #         'name': instance.name,
    #         'id_detail': instance.id_detail.identification_number,
    #         'email': instance.email,
    #         'password': instance.password
    #     }

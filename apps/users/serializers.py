from rest_framework import serializers
from .models import User, UserAdditionalInfo
from rest_framework_simplejwt.tokens import RefreshToken

class UserAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdditionalInfo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user_additional_info = UserAdditionalInfoSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'middle_name', 'type', 'phone', 'sms_notification', 'user_additional_info']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_additional_info_data = validated_data.pop('user_additional_info', None)
        user = User.objects.create(**validated_data)
        if user_additional_info_data:
            UserAdditionalInfo.objects.create(user=user, **user_additional_info_data)
        return user

    def update(self, instance, validated_data):
        user_additional_info_data = validated_data.pop('user_additional_info', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if user_additional_info_data:
            user_additional_info = instance.user_additional_info
            for attr, value in user_additional_info_data.items():
                setattr(user_additional_info, attr, value)
            user_additional_info.save()

        return instance
    

class TokenObtainPairSerializer(serializers.Serializer):
    """
    Serializer для получения пары токенов (access и refresh)
    """
    access = serializers.CharField()
    refresh = serializers.CharField()
    

class TokenRefreshSerializer(serializers.Serializer):
    """
    Serializer для обновления access токена
    """
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        return data






































































# from rest_framework import serializers
# from .models import User, UserAdditionalInfo

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'username', 'middle_name', 'type', 'phone', 'groups', 'user_permissions', 'sms_notification']

# class UserAdditionalInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAdditionalInfo
#         fields = ['id', 'user', 'date_of_birth', 'sex', 'passport_photo_reversal', 'passport_photo_registered_address', 'registered_address', 'passport_series', 'passport_number', 'subdivision_code', 'date_of_issue']



































































































# from rest_framework import serializers
# from .models import User, UserAdditionalInfo

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'type', 'phone', 'sms_notification']

# class UserAdditionalInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAdditionalInfo
#         fields = ['id', 'user', 'date_of_birth', 'sex', 'passport_photo_reversal', 'passport_photo_registered_address',
#                   'registered_address', 'passport_series', 'passport_number', 'subdivision_code', 'date_of_issue']



from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserAuthenticationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class EmailVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
























































































































# # from rest_framework import serializers
# # from django.contrib.auth.models import User


# # class UserRegistrationSerializer(serializers.Serializer):
# #     username = serializers.CharField(max_length=150)
# #     email = serializers.EmailField()
# #     # password = serializers.CharField()
# #     password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    
# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password']  
        

# #     def create(self, validated_data):
# #         # Создание пользователя с помощью введенных данных
# #         # user = user.objects.create_user(**validated_data)
# #         user = User.objects.create_user(**validated_data)

# #         return user

# # class UserAuthenticationSerializer(serializers.Serializer):
# #     username = serializers.CharField(max_length=150)
# #     password = serializers.CharField()

# # class EmailVerificationSerializer(serializers.Serializer):
# #     token = serializers.CharField()

# # class PasswordResetSerializer(serializers.Serializer):
# #     email = serializers.EmailField()

# # class UserProfileSerializer(serializers.Serializer):
# #     username = serializers.CharField(max_length=150)
# #     email = serializers.EmailField()
# #     email_confirmed = serializers.BooleanField()

























































# # # from rest_framework import serializers

# # # class UserRegistrationSerializer(serializers.Serializer):
# # #     username = serializers.CharField(max_length=150)
# # #     email = serializers.EmailField()
# # #     password = serializers.CharField()

# # # class UserAuthenticationSerializer(serializers.Serializer):
# # #     username = serializers.CharField(max_length=150)
# # #     password = serializers.CharField()

# # # class EmailVerificationSerializer(serializers.Serializer):
# # #     token = serializers.CharField()

# # # class PasswordResetSerializer(serializers.Serializer):
# # #     email = serializers.EmailField()

# # # class UserProfileSerializer(serializers.Serializer):
# # #     username = serializers.CharField(max_length=150)
# # #     email = serializers.EmailField()
# # #     email_confirmed = serializers.BooleanField()




















































































# # # # from rest_framework import serializers
# # # # from rest_framework.authtoken.models import Token
# # # # from django.contrib.auth import authenticate
# # # # from .models import *

# # # # class UserRegistrationSerializer(serializers.ModelSerializer):
# # # #     password = serializers.CharField(write_only=True)

# # # #     class Meta:
# # # #         model = CustomUser
# # # #         fields = ('email', 'username', 'password')

# # # #     def create(self, validated_data):
# # # #         user = CustomUser.objects.create_user(**validated_data)
# # # #         return user

# # # # class UserAuthenticationSerializer(serializers.Serializer):
# # # #     email = serializers.EmailField()
# # # #     password = serializers.CharField(style={'input_type': 'password'})

# # # #     def validate(self, attrs):
# # # #         email = attrs.get('email')
# # # #         password = attrs.get('password')
# # # #         user = authenticate(email=email, password=password)
# # # #         if not user:
# # # #             raise serializers.ValidationError('Incorrect email or password')
# # # #         attrs['user'] = user
# # # #         return attrs

# # # # class EmailVerificationSerializer(serializers.Serializer):
# # # #     token = serializers.CharField()

# # # # class PasswordResetSerializer(serializers.Serializer):
# # # #     email = serializers.EmailField()

# # # # class UserProfileSerializer(serializers.ModelSerializer):
# # # #     class Meta:
# # # #         model = CustomUser
# # # #         fields = ('email', 'username')

# # # #     def update(self, instance, validated_data):
# # # #         instance.email = validated_data.get('email', instance.email)
# # # #         instance.username = validated_data.get('username', instance.username)
# # # #         instance.save()
# # # #         return instance

# # # #     def to_representation(self, instance):
# # # #         data = super().to_representation(instance)
# # # #         data['is_staff'] = instance.is_staff
# # # #         data['is_active'] = instance.is_active
# # # #         return data








































# # # # # class UserSerializer(serializers.ModelSerializer):
# # # # #     class Meta:
# # # # #         model = CustomUser
# # # # #         fields = ['id', 'email', 'username', 'password']
# # # # #         extra_kwargs = {'password': {'write_only': True}}

# # # # #     def create(self, validated_data):
# # # # #         user = CustomUser.objects.create_user(**validated_data)
# # # # #         return user


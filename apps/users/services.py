from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import gettext_lazy as _
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth.models import User

# class UserService:
#     @staticmethod
#     def create_user(email, password, username=None):
#         """
#         Создание нового пользователя
#         """
#         # Проверка наличия пользователя с таким же email
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Пользователь с таким email уже существует")
        
#         # Генерация хэша пароля перед сохранением
#         hashed_password = make_password(password)
        
#         # Создание пользователя с использованием хэшированного пароля
#         user = User.objects.create(email=email, password=hashed_password)
        
#         # Установка некоторых значений по умолчанию
#         user.is_active = True  # Пользователь активен сразу после создания
#         user.is_staff = False  # Пользователь не является персоналом (staff)
        
#         # Установка пользовательского имени, если указано
#         if username:
#             user.username = username
        
#         user.save()
        
#         # Отправка письма подтверждения по электронной почте
#         subject = 'Подтверждение регистрации'
#         message = 'Вы успешно зарегистрированы на нашем сайте. Спасибо за регистрацию!'
#         from_email = 'noreply@example.com'  # Укажите вашу почту
#         recipient_list = [email]
#         send_mail(subject, message, from_email, recipient_list)

#         return user



class UserService:
    @staticmethod
    def create_user(email, password, username=None):
        """
        Создание нового пользователя
        """
        # Проверка наличия пользователя с таким же email
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует")
        
        # Создание пользователя
        user = User.objects.create_user(email=email, password=password, username=username)
        
        return user

    @staticmethod
    def get_user_by_email(email):
        """
        Получение пользователя по email
        """
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def send_confirmation_email(user):
        """
        Отправка письма подтверждения по электронной почте
        """
        subject = 'Подтверждение регистрации'
        message = f'Здравствуйте, {user.username}!\n\n'
        message += 'Вы успешно зарегистрированы на нашем сайте. Спасибо за регистрацию!\n\n'
        message += 'С уважением,\nКоманда сайта'
        
        send_mail(subject, message, 'noreply@example.com', [user.email], fail_silently=False)




# def register_user(data):
#     """
#     Регистрирует нового пользователя.

#     Args:
#         data (dict): Словарь с данными нового пользователя.

#     Returns:
#         dict: Результат операции регистрации пользователя.    
        
#     """
    
    
from django.contrib.auth import get_user_model
from .tasks import send_email_task

User = get_user_model()

def register_user(request):
    if request.method == 'POST':
        # Обработка данных формы регистрации
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Создание пользователя
        user = User.objects.create_user(username=username, email=email, password=password)

        # Отправка письма для подтверждения регистрации
        subject = 'Подтверждение регистрации'
        message = 'Спасибо за регистрацию!'
        recipient_list = [email]
        send_email_task.delay(subject, message, recipient_list)
        
        # Вернуть какой-то ответ или перенаправить пользователя

    
    
    
    
    # Инициализация сериализатора для регистрации пользователя
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        # Сохранение пользователя, если данные валидны
        serializer.save()
        return {'success': True, 'message': 'User registered successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def authenticate_user(data):
    """
    Аутентифицирует пользователя и выдает токен аутентификации.

    Args:
        data (dict): Словарь с данными для аутентификации.

    Returns:
        dict: Результат операции аутентификации.
    """
    email = data.get('email')
    password = data.get('password')

    # Проверяем, существует ли пользователь с такой электронной почтой
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return {'success': False, 'message': 'Incorrect email or password'}

    # Проверяем пароль
    user = authenticate(email=email, password=password)
    if user is not None:
        # Логин пользователя и создание или получение токена аутентификации
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return {'success': True, 'token': token.key}
    else:
        return {'success': False, 'message': 'Incorrect email or password'}

def verify_email(data):
    """
    Подтверждает электронную почту пользователя по токену.

    Args:
        data (dict): Словарь с данными для подтверждения email.

    Returns:
        dict: Результат операции подтверждения email.
    """
    serializer = EmailVerificationSerializer(data=data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        # Здесь будет ваша логика подтверждения email
        return {'success': True, 'message': 'Email verified successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def reset_password(data):
    """
    Сбрасывает пароль пользователя и отправляет письмо с инструкциями для сброса пароля.

    Args:
        data (dict): Словарь с данными для сброса пароля.

    Returns:
        dict: Результат операции сброса пароля.
    """
    serializer = PasswordResetSerializer(data=data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        try:
            # Пытаемся найти пользователя по электронной почте
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Если пользователь не найден, возвращаем ошибку
            return {'success': False, 'errors': {'email': _('Пользователь с этим адресом электронной почты не существует.')}}

        # Генерируем уникальный токен для сброса пароля
        token = default_token_generator.make_token(user)

        # Создаем ссылку для сброса пароля
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f"http://yourdomain.com/reset-password/{uid}/{token}/"

        # Отправляем письмо с инструкциями для сброса пароля
        subject = 'Сброс пароля'
        message = render_to_string('reset_password_email.html', {
            'user': user,
            'reset_url': reset_url,
        })
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [email])

        return {'success': True, 'message': _('Письмо для сброса пароля отправлено. Пожалуйста, проверьте вашу почту.')}
    else:
        return {'success': False, 'errors': serializer.errors}



def update_user_profile(user, data):
    """
    Обновляет профиль пользователя.

    Args:
        user (User): Объект пользователя, чей профиль нужно обновить.
        data (dict): Словарь с данными для обновления профиля.

    Returns:
        dict: Результат операции обновления профиля.
    """
    # Получение или создание профиля пользователя
    profile, created = UserProfile.objects.get_or_create(user=user)

    # Инициализация сериализатора для обновления профиля пользователя
    serializer = UserProfileSerializer(profile, data=data)
    if serializer.is_valid():
        # Сохранение обновленных данных профиля пользователя
        serializer.save()
        return {'success': True, 'message': 'User profile updated successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}










































































































# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from .models import User
# # from .serializers import UserRegistrationSerializer, EmailVerificationSerializer, PasswordResetSerializer, UserProfileSerializer

# def register_user(data):
#     # Инициализация сериализатора для регистрации пользователя
#     serializer = UserRegistrationSerializer(data=data)
#     if serializer.is_valid():
#         # Сохранение пользователя, если данные валидны
#         serializer.save()
#         return {'success': True, 'message': 'User registered successfully'}
#     else:
#         return {'success': False, 'errors': serializer.errors}

# def authenticate_user(data):
#     email = data.get('email')
#     password = data.get('password')
#     # Аутентификация пользователяaxd
#     user = authenticate(email=email, password=password)
#     if user is not None:
#         # Логин пользователя и создание или получение токена аутентификации
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return {'success': True, 'token': token.key}
#     else:
#         return {'success': False, 'message': 'Incorrect email or password'}

# def verify_email(data):
#     serializer = EmailVerificationSerializer(data=data)
#     if serializer.is_valid():
#         token = serializer.validated_data['token']
#         # Здесь будет ваша логика подтверждения email
#         return {'success': True, 'message': 'Email verified successfully'}
#     else:
#         return {'success': False, 'errors': serializer.errors}

# def reset_password(data):
#     serializer = PasswordResetSerializer(data=data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         # Здесь будет ваша логика сброса пароля
#         return {'success': True, 'message': 'Password reset email sent'}
#     else:
#         return {'success': False, 'errors': serializer.errors}

# def update_user_profile(user, data):
#     # Инициализация сериализатора для обновления профиля пользователя
#     serializer = UserProfileSerializer(user, data=data)
#     if serializer.is_valid():
#         # Сохранение обновленных данных профиля пользователя
#         serializer.save()
#         return {'success': True, 'message': 'User profile updated successfully'}
#     else:
#         return {'success': False, 'errors': serializer.errors}






















































































# # from django.contrib.auth import authenticate, login
# # from rest_framework.authtoken.models import Token
# # from .models import User
# # # from .serializers import UserSerializer, UserAdditionalInfoSerializer

# # from .serializers import UserRegistrationSerializer, EmailVerificationSerializer, PasswordResetSerializer, UserProfileSerializer




# # def register_user(data):
# #     serializer = UserRegistrationSerializer(data=data)
# #     if serializer.is_valid():
# #         serializer.save()
# #         return {'success': True, 'message': 'User registered successfully'}
# #     else:
# #         return {'success': False, 'errors': serializer.errors}

# # def authenticate_user(data):
# #     email = data.get('email')
# #     password = data.get('password')
# #     user = authenticate(email=email, password=password)
# #     if user is not None:
# #         login(request, user)
# #         token, created = Token.objects.get_or_create(user=user)
# #         return {'success': True, 'token': token.key}
# #     else:
# #         return {'success': False, 'message': 'Incorrect email or password'}

# # def verify_email(data):
# #     serializer = EmailVerificationSerializer(data=data)
# #     if serializer.is_valid():
# #         token = serializer.validated_data['token']
# #         # Здесь будет ваша логика подтверждения email
# #         return {'success': True, 'message': 'Email verified successfully'}
# #     else:
# #         return {'success': False, 'errors': serializer.errors}

# # def reset_password(data):
# #     serializer = PasswordResetSerializer(data=data)
# #     if serializer.is_valid():
# #         email = serializer.validated_data['email']
# #         # Здесь будет ваша логика сброса пароля
# #         return {'success': True, 'message': 'Password reset email sent'}
# #     else:
# #         return {'success': False, 'errors': serializer.errors}

# # def update_user_profile(user, data):
# #     serializer = UserProfileSerializer(user, data=data)
# #     if serializer.is_valid():
# #         serializer.save()
# #         return {'success': True, 'message': 'User profile updated successfully'}
# #     else:
# #         return {'success': False, 'errors': serializer.errors}











































































# # # from django.contrib.auth import authenticate, login
# # # from rest_framework.authtoken.models import Token
# # # from django.core.exceptions import ValidationError
# # # from .models import CustomUser
# # # from .serializers import *

# # # def register_user(data):
# # #     serializer = UserRegistrationSerializer(data=data)
# # #     if serializer.is_valid():
# # #         serializer.save()
# # #         return {'success': True, 'message': 'User registered successfully'}
# # #     else:
# # #         return {'success': False, 'errors': serializer.errors}

# # # def authenticate_user(data):
# # #     email = data.get('email')
# # #     password = data.get('password')
# # #     user = authenticate(email=email, password=password)
# # #     if user is not None:
# # #         login(request, user)
# # #         token, created = Token.objects.get_or_create(user=user)
# # #         return {'success': True, 'token': token.key}
# # #     else:
# # #         return {'success': False, 'message': 'Incorrect email or password'}

# # # def verify_email(data):
# # #     serializer = EmailVerificationSerializer(data=data)
# # #     if serializer.is_valid():
# # #         token = serializer.validated_data['token']
# # #         # Your email verification logic here
# # #         return {'success': True, 'message': 'Email verified successfully'}
# # #     else:
# # #         return {'success': False, 'errors': serializer.errors}

# # # def reset_password(data):
# # #     serializer = PasswordResetSerializer(data=data)
# # #     if serializer.is_valid():
# # #         email = serializer.validated_data['email']
# # #         # Your password reset logic here
# # #         return {'success': True, 'message': 'Password reset email sent'}
# # #     else:
# # #         return {'success': False, 'errors': serializer.errors}

# # # def update_user_profile(user, data):
# # #     serializer = UserProfileSerializer(user, data=data)
# # #     if serializer.is_valid():
# # #         serializer.save()
# # #         return {'success': True, 'message': 'User profile updated successfully'}
# # #     else:
# # #         return {'success': False, 'errors': serializer.errors}

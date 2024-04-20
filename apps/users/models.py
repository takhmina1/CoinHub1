from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission



class User(AbstractUser):
    """Пользователь"""

    USER = 'user'
    ADMIN = 'admin'

    TYPE = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
    )

    username = models.EmailField(verbose_name='Логин', max_length=255, unique=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=150, blank=True, null=True)
    type = models.CharField(verbose_name='Тип аккаунта', choices=TYPE, max_length=20, default=USER)
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=19,
        validators=[
            MinLengthValidator(19),
            RegexValidator(regex=r'^\+?1?\d{11}$', message='Телефон должен быть в формате: +996999999900')
        ],
        unique=True,
        blank=True,
        null=True
    )
    
    
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='my_custom_related_name')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='my_custom_related_name')
    
    sms_notification = models.BooleanField(verbose_name='Уведомление по смс', default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.id} | {self.first_name} | {self.last_name} | {self.username}'

class UserAdditionalInfo(models.Model):
    """Дополнительная информация о пользователе"""

    M = "Муж"
    W = "Жен"

    SEX = (
        (M, "Мужской"),
        (W, "Женский")
    )

    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        default='',
        null=True,
        blank=True
    )

    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    sex = models.CharField(verbose_name='Пол', choices=SEX, max_length=30, default=M, blank=True)
    passport_photo_reversal = models.ImageField(
        verbose_name='Фото разворота паспорта',
        upload_to='passport_photo_reversal',
        blank=True,
    ) 
    passport_photo_registered_address = models.ImageField(
        verbose_name='Фото страницы с пропиской',
        upload_to='passport_photo_reversal',
        blank=True,
    )
    registered_address = models.CharField(verbose_name='Прописка', max_length=250, null=True, blank=True)
    passport_series = models.CharField(
        verbose_name='Серия паспорта',
        validators=[MinLengthValidator(4), RegexValidator("^[0-9]+$")],
        max_length=4,
        null=True,
        blank=True,
    )
    passport_number = models.CharField(
        verbose_name='Номер паспорта',
        validators=[MinLengthValidator(6), RegexValidator("^[0-9]+$")],
        max_length=6,
        default='',
    )
    subdivision_code = models.CharField(
        verbose_name='Код подразделения',
        validators=[MinLengthValidator(7)],
        max_length=7,
        default='',
    )
    date_of_issue = models.DateField(verbose_name='Дата выдачи паспорта', null=True, blank=True)

    class Meta:
        verbose_name = 'Дополнительная информация о пользователе'
        verbose_name_plural = 'Дополнительная информация о пользователе'

    def __str__(self):
        if self.user:
            return f'{self.id} | {self.user.first_name} | {self.user.last_name} | {self.user.username}'








# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


































































































# from django.db import models
# from django.contrib.auth.hashers import make_password, check_password

# class CustomUser(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)  # Хранение пароля в зашифрованном виде
#     email_confirmed = models.BooleanField(default=False)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)  # Хеширование пароля перед сохранением

#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)  # Проверка пароля

#     @classmethod
#     def register_user(cls, username, email, password):
#         if cls.objects.filter(username=username).exists():
#             return "Пользователь с таким именем уже существует"
#         if cls.objects.filter(email=email).exists():
#             return "Пользователь с такой почтой уже существует"
#         new_user = cls(username=username, email=email)
#         new_user.set_password(password)
#         new_user.save()
#         return "Пользователь успешно зарегистрирован"

#     @classmethod
#     def authenticate_user(cls, username, password):
#         user = cls.objects.filter(username=username).first()
#         if user and user.check_password(password):
#             return user
#         return None

#     @classmethod
#     def confirm_email(cls, email):
#         user = cls.objects.filter(email=email).first()
#         if user:
#             user.email_confirmed = True
#             user.save()
#             return "Email успешно подтвержден"
#         return "Пользователь с такой почтой не найден"

#     @classmethod
#     def reset_password(cls, email, new_password):
#         user = cls.objects.filter(email=email).first()
#         if user:
#             user.set_password(new_password)
#             user.save()
#             return "Пароль успешно изменен"
#         return "Пользователь с такой почтой не найден"

#     @classmethod
#     def change_password(cls, username, old_password, new_password):
#         user = cls.objects.filter(username=username).first()
#         if user and user.check_password(old_password):
#             user.set_password(new_password)
#             user.save()
#             return "Пароль успешно изменен"
#         return "Пользователь с таким именем и паролем не найден"




























# # from django.db import models
# # from django.contrib.auth.hashers import make_password, check_password

# # class CustomUser(models.Model):
# #     username = models.CharField(max_length=150, unique=True)
# #     email = models.EmailField(unique=True)
# #     password = models.CharField(max_length=128)  # Хранение пароля в зашифрованном виде
# #     email_confirmed = models.BooleanField(default=False)

# #     def set_password(self, raw_password):
# #         self.password = make_password(raw_password)  # Хеширование пароля перед сохранением

# #     def check_password(self, raw_password):
# #         return check_password(raw_password, self.password)  # Проверка пароля

# #     @classmethod
# #     def register_user(cls, username, email, password):
# #         if cls.objects.filter(username=username).exists():
# #             return "Пользователь с таким именем уже существует"
# #         if cls.objects.filter(email=email).exists():
# #             return "Пользователь с такой почтой уже существует"
# #         new_user = cls(username=username, email=email)
# #         new_user.set_password(password)
# #         new_user.save()
# #         return "Пользователь успешно зарегистрирован"

# #     @classmethod
# #     def authenticate_user(cls, username, password):
# #         user = cls.objects.filter(username=username).first()
# #         if user and user.check_password(password):
# #             return user
# #         return None

# #     @classmethod
# #     def confirm_email(cls, email):
# #         user = cls.objects.filter(email=email).first()
# #         if user:
# #             user.email_confirmed = True
# #             user.save()
# #             return "Email успешно подтвержден"
# #         return "Пользователь с такой почтой не найден"

# #     @classmethod
# #     def reset_password(cls, email, new_password):
# #         user = cls.objects.filter(email=email).first()
# #         if user:
# #             user.set_password(new_password)
# #             user.save()
# #             return "Пароль успешно изменен"
# #         return "Пользователь с такой почтой не найден"

# #     @classmethod
# #     def change_password(cls, username, old_password, new_password):
# #         user = cls.objects.filter(username=username).first()
# #         if user and user.check_password(old_password):
# #             user.set_password(new_password)
# #             user.save()
# #             return "Пароль успешно изменен"
# #         return "Пользователь с таким именем и паролем не найден"







































































































































# # # from django.db import models
# # # from django.utils import timezone
# # # from django.core.mail import send_mail
# # # from django.conf import settings
# # # import uuid

# # # class CustomUserManager(models.Manager):
# # #     def create_user(self, email, username, password=None, **extra_fields):
# # #         if not email:
# # #             raise ValueError('The Email field must be set')
# # #         email = self.normalize_email(email)
# # #         user = self.model(email=email, username=username, **extra_fields)
# # #         user.set_password(password)
# # #         user.save(using=self._db)
# # #         return user

# # #     def create_superuser(self, email, username, password=None, **extra_fields):
# # #         extra_fields.setdefault('is_staff', True)
# # #         extra_fields.setdefault('is_superuser', True)
# # #         if extra_fields.get('is_staff') is not True:
# # #             raise ValueError('Superuser must have is_staff=True.')
# # #         if extra_fields.get('is_superuser') is not True:
# # #             raise ValueError('Superuser must have is_superuser=True.')
# # #         return self.create_user(email, username, password, **extra_fields)


# # # class CustomUser(models.Model):
# # #     email = models.EmailField('email address', unique=True)
# # #     username = models.CharField('username', max_length=150, unique=True)
# # #     is_active = models.BooleanField('active', default=True)
# # #     is_staff = models.BooleanField('staff status', default=False)
# # #     date_joined = models.DateTimeField('date joined', default=timezone.now)

# # #     USERNAME_FIELD = 'email'
# # #     REQUIRED_FIELDS = ['username']

# # #     objects = CustomUserManager()

# # #     def __str__(self):
# # #         return self.email

# # #     def get_full_name(self):
# # #         return self.username

# # #     def get_short_name(self):
# # #         return self.username


# # # class EmailVerificationToken(models.Model):
# # #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # #     token = models.UUIDField(default=uuid.uuid4, editable=False)
# # #     created_at = models.DateTimeField(auto_now_add=True)

# # #     def __str__(self):
# # #         return f"Verification Token for {self.user.email}"

# # #     def send_verification_email(self):
# # #         subject = 'Email Verification'
# # #         message = f'Use this token to verify your email: {self.token}'
# # #         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.user.email])


# # # class PasswordResetToken(models.Model):
# # #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # #     token = models.UUIDField(default=uuid.uuid4, editable=False)
# # #     created_at = models.DateTimeField(auto_now_add=True)

# # #     def __str__(self):
# # #         return f"Password Reset Token for {self.user.email}"

# # #     def send_reset_email(self):
# # #         subject = 'Password Reset'
# # #         message = f'Use this token to reset your password: {self.token}'
# # #         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.user.email])










































































# # # # from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # # # from django.db import models
# # # # from django.utils import timezone
# # # # from django.core.mail import send_mail
# # # # from django.utils.translation import gettext_lazy as _
# # # # from django.conf import settings
# # # # import uuid

# # # # class CustomUserManager(BaseUserManager):
# # # #     def create_user(self, email, username, password=None, **extra_fields):
# # # #         if not email:
# # # #             raise ValueError(_('The Email field must be set'))
# # # #         email = self.normalize_email(email)
# # # #         user = self.model(email=email, username=username, **extra_fields)
# # # #         user.set_password(password)
# # # #         user.save(using=self._db)
# # # #         return user

# # # #     def create_superuser(self, email, username, password=None, **extra_fields):
# # # #         extra_fields.setdefault('is_staff', True)
# # # #         extra_fields.setdefault('is_superuser', True)
# # # #         if extra_fields.get('is_staff') is not True:
# # # #             raise ValueError(_('Superuser must have is_staff=True.'))
# # # #         if extra_fields.get('is_superuser') is not True:
# # # #             raise ValueError(_('Superuser must have is_superuser=True.'))
# # # #         return self.create_user(email, username, password, **extra_fields)


# # # # class CustomUser(AbstractBaseUser):
# # # #     email = models.EmailField(_('email address'), unique=True)
# # # #     username = models.CharField(_('username'), max_length=150, unique=True)
# # # #     is_active = models.BooleanField(_('active'), default=True)
# # # #     is_staff = models.BooleanField(_('staff status'), default=False)
# # # #     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

# # # #     USERNAME_FIELD = 'email'
# # # #     REQUIRED_FIELDS = ['username']

# # # #     objects = CustomUserManager()

# # # #     def __str__(self):
# # # #         return self.email

# # # #     def get_full_name(self):
# # # #         return self.username

# # # #     def get_short_name(self):
# # # #         return self.username


# # # # class EmailVerificationToken(models.Model):
# # # #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # # #     token = models.UUIDField(default=uuid.uuid4, editable=False)
# # # #     created_at = models.DateTimeField(auto_now_add=True)

# # # #     def __str__(self):
# # # #         return f"Verification Token for {self.user.email}"

# # # #     def send_verification_email(self):
# # # #         subject = 'Email Verification'
# # # #         message = f'Use this token to verify your email: {self.token}'
# # # #         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.user.email])


# # # # class PasswordResetToken(models.Model):
# # # #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # # #     token = models.UUIDField(default=uuid.uuid4, editable=False)
# # # #     created_at = models.DateTimeField(auto_now_add=True)

# # # #     def __str__(self):
# # # #         return f"Password Reset Token for {self.user.email}"

# # # #     def send_reset_email(self):
# # # #         subject = 'Password Reset'
# # # #         message = f'Use this token to reset your password: {self.token}'
# # # #         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.user.email])

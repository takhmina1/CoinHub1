from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from .services import (register_user, authenticate_user, verify_email,
                       reset_password, update_user_profile)
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={
            201: "User registered successfully",
            400: "Bad Request"
        },
        operation_summary="User Registration",
        operation_description="Registers a new user with the provided credentials."
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = register_user(request.data)
            if response['success']:
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAuthenticationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserAuthenticationSerializer

    @swagger_auto_schema(
        request_body=UserAuthenticationSerializer,
        responses={
            200: "User authenticated successfully",
            401: "Unauthorized",
            400: "Bad Request"
        },
        operation_summary="User Authentication",
        operation_description="Authenticates a user with the provided credentials."
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = authenticate_user(request.data)
            if response['success']:
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailVerificationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailVerificationSerializer

    @swagger_auto_schema(
        request_body=EmailVerificationSerializer,
        responses={
            200: "Email verified successfully",
            400: "Bad Request"
        },
        operation_summary="Email Verification",
        operation_description="Verifies the email address with the provided token."
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = verify_email(request.data)
            if response['success']:
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    @swagger_auto_schema(
        request_body=PasswordResetSerializer,
        responses={
            200: "Password reset successful",
            400: "Bad Request"
        },
        operation_summary="Password Reset",
        operation_description="Resets the password for the user."
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = reset_password(request.data)
            if response['success']:
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

class ObtainTokenPairView(TokenObtainPairView):
    """
    Представление для получения пары токенов (access и refresh)
    """
    serializer_class = TokenObtainPairSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response('Successful token obtainment', TokenObtainPairSerializer)},
        tags=['Authentication'],
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class RefreshTokenView(TokenRefreshView):
    """
    Представление для обновления access токена
    """
    serializer_class = TokenRefreshSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response('Successful token refresh', TokenObtainPairSerializer)},
        tags=['Authentication'],
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

        responses={
            200: "User profile retrieved successfully",
            400: "Bad Request"
        },
        operation_summary="Get User Profile",
        operation_description="Retrieves the profile information of the authenticated user."
    
    
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UserProfileSerializer,
        responses={
            200: "User profile updated successfully",
            400: "Bad Request"
        },
        operation_summary="Update User Profile",
        operation_description="Updates the profile information of the authenticated user."
    )
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid():
            response = update_user_profile(request.user, request.data)
            if response['success']:
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ObtainTokenPairView(TokenObtainPairView):
    """
    Представление для получения пары токенов (access и refresh)
    """
    serializer_class = TokenObtainPairSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response('Successful token obtainment', TokenObtainPairSerializer)},
        tags=['Authentication'],
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

class RefreshTokenView(TokenRefreshView):
    """
    Представление для обновления access токена
    """
    serializer_class = TokenRefreshSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response('Successful token refresh', TokenObtainPairSerializer)},
        tags=['Authentication'],
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


























































# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .serializers import (UserRegistrationSerializer, UserAuthenticationSerializer,
#                           EmailVerificationSerializer, PasswordResetSerializer,
#                           UserProfileSerializer)
# from .services import (register_user, authenticate_user, verify_email,
#                        reset_password, update_user_profile)
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# class UserRegistrationView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserRegistrationSerializer

#     @swagger_auto_schema(
#         request_body=UserRegistrationSerializer,
#         responses={
#             201: "User registered successfully",
#             400: "Bad Request"
#         },
#         operation_summary="User Registration",
#         operation_description="Registers a new user with the provided credentials."
#     )
#     def post(self, request):
#         """
#         Registers a new user with the provided credentials.
#         """
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             response = register_user(request.data)
#             if response['success']:
#                 return Response(response, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserAuthenticationView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserAuthenticationSerializer

#     @swagger_auto_schema(
#         request_body=UserAuthenticationSerializer,
#         responses={
#             200: "User authenticated successfully",
#             401: "Unauthorized",
#             400: "Bad Request"
#         },
#         operation_summary="User Authentication",
#         operation_description="Authenticates a user with the provided credentials."
#     )
#     def post(self, request):
#         """
#         Authenticates a user with the provided credentials.
#         """
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             response = authenticate_user(request.data)
#             if response['success']:
#                 return Response(response, status=status.HTTP_200_OK)
#             else:
#                 return Response(response, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmailVerificationView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = EmailVerificationSerializer

#     @swagger_auto_schema(
#         request_body=EmailVerificationSerializer,
#         responses={
#             200: "Email verified successfully",
#             400: "Bad Request"
#         },
#         operation_summary="Email Verification",
#         operation_description="Verifies the email address with the provided token."
#     )
#     def post(self, request):
#         """
#         Verifies the email address with the provided token.
#         """
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             response = verify_email(request.data)
#             if response['success']:
#                 return Response(response, status=status.HTTP_200_OK)
#             else:
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PasswordResetView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = PasswordResetSerializer

#     @swagger_auto_schema(
#         request_body=PasswordResetSerializer,
#         responses={
#             200: "Password reset successful",
#             400: "Bad Request"
#         },
#         operation_summary="Password Reset",
#         operation_description="Resets the password for the user."
#     )
#     def post(self, request):
#         """
#         Resets the password for the user.
#         """
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             response = reset_password(request.data)
#             if response['success']:
#                 return Response(response, status=status.HTTP_200_OK)
#             else:
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserProfileView(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserProfileSerializer

#     @swagger_auto_schema(
#         responses={
#             200: "User profile retrieved successfully",
#             400: "Bad Request"
#         },
#         operation_summary="Get User Profile",
#         operation_description="Retrieves the profile information of the authenticated user."
#     )
#     def get(self, request):
#         """
#         Retrieves the profile information of the authenticated user.
#         """
#         serializer = self.serializer_class(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     @swagger_auto_schema(
#         request_body=UserProfileSerializer,
#         responses={
#             200: "User profile updated successfully",
#             400: "Bad Request"
#         },
#         operation_summary="Update User Profile",
#         operation_description="Updates the profile information of the authenticated user."
#     )
#     def put(self, request):
#         """
#         Updates the profile information of the authenticated user.
#         """
#         serializer = self.serializer_class(request.user, data=request.data)
#         if serializer.is_valid():
#             response = update_user_profile(request.user, request.data)
#             if response['success']:
#                 return Response(response, status=status.HTTP_200_OK)
#             else:
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




































































































# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.permissions import AllowAny, IsAuthenticated
# # from .serializers import (UserRegistrationSerializer, UserAuthenticationSerializer,
# #                           EmailVerificationSerializer, PasswordResetSerializer,
# #                           UserProfileSerializer)
# # from .services import (register_user, authenticate_user, verify_email,
# #                        reset_password, update_user_profile)

# # class UserRegistrationView(APIView):
# #     permission_classes = (AllowAny,)
# #     serializer_class = UserRegistrationSerializer

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             response = register_user(request.data)
# #             if response['success']:
# #                 return Response(response, status=status.HTTP_201_CREATED)
# #             else:
# #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class UserAuthenticationView(APIView):
# #     permission_classes = (AllowAny,)
# #     serializer_class = UserAuthenticationSerializer

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             response = authenticate_user(request.data)
# #             if response['success']:
# #                 return Response(response, status=status.HTTP_200_OK)
# #             else:
# #                 return Response(response, status=status.HTTP_401_UNAUTHORIZED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class EmailVerificationView(APIView):
# #     permission_classes = (AllowAny,)
# #     serializer_class = EmailVerificationSerializer

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             response = verify_email(request.data)
# #             if response['success']:
# #                 return Response(response, status=status.HTTP_200_OK)
# #             else:
# #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class PasswordResetView(APIView):
# #     permission_classes = (AllowAny,)
# #     serializer_class = PasswordResetSerializer

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             response = reset_password(request.data)
# #             if response['success']:
# #                 return Response(response, status=status.HTTP_200_OK)
# #             else:
# #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class UserProfileView(APIView):
# #     permission_classes = (IsAuthenticated,)
# #     serializer_class = UserProfileSerializer

# #     def get(self, request):
# #         serializer = self.serializer_class(request.user)
# #         return Response(serializer.data, status=status.HTTP_200_OK)

# #     def put(self, request):
# #         serializer = self.serializer_class(request.user, data=request.data)
# #         if serializer.is_valid():
# #             response = update_user_profile(request.user, request.data)
# #             if response['success']:
# #                 return Response(response, status=status.HTTP_200_OK)
# #             else:
# #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



























































































































































































# # # from rest_framework import status
# # # from rest_framework.response import Response
# # # from rest_framework.views import APIView
# # # from rest_framework.permissions import AllowAny, IsAuthenticated
# # # from .serializers import (UserRegistrationSerializer, UserAuthenticationSerializer,
# # #                           EmailVerificationSerializer, PasswordResetSerializer,
# # #                           UserProfileSerializer)
# # # from .services import (register_user, authenticate_user, verify_email,
# # #                        reset_password, update_user_profile)

# # # class UserRegistrationView(APIView):
# # #     permission_classes = (AllowAny,)
# # #     serializer_class = UserRegistrationSerializer  # Определение сериализатора для запроса

# # #     def post(self, request):
# # #         serializer = self.serializer_class(data=request.data)
# # #         if serializer.is_valid():
# # #             response = register_user(request.data)
# # #             if response['success']:
# # #                 return Response(response, status=status.HTTP_201_CREATED)
# # #             else:
# # #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class UserAuthenticationView(APIView):
# # #     permission_classes = (AllowAny,)
# # #     serializer_class = UserAuthenticationSerializer  # Определение сериализатора для запроса

# # #     def post(self, request):
# # #         serializer = self.serializer_class(data=request.data)
# # #         if serializer.is_valid():
# # #             response = authenticate_user(request.data)
# # #             if response['success']:
# # #                 return Response(response, status=status.HTTP_200_OK)
# # #             else:
# # #                 return Response(response, status=status.HTTP_401_UNAUTHORIZED)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class EmailVerificationView(APIView):
# # #     permission_classes = (AllowAny,)
# # #     serializer_class = EmailVerificationSerializer  # Определение сериализатора для запроса

# # #     def post(self, request):
# # #         serializer = self.serializer_class(data=request.data)
# # #         if serializer.is_valid():
# # #             response = verify_email(request.data)
# # #             if response['success']:
# # #                 return Response(response, status=status.HTTP_200_OK)
# # #             else:
# # #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class PasswordResetView(APIView):
# # #     permission_classes = (AllowAny,)
# # #     serializer_class = PasswordResetSerializer  # Определение сериализатора для запроса

# # #     def post(self, request):
# # #         serializer = self.serializer_class(data=request.data)
# # #         if serializer.is_valid():
# # #             response = reset_password(request.data)
# # #             if response['success']:
# # #                 return Response(response, status=status.HTTP_200_OK)
# # #             else:
# # #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class UserProfileView(APIView):
# # #     permission_classes = (IsAuthenticated,)
# # #     serializer_class = UserProfileSerializer  # Определение сериализатора для запроса

# # #     def get(self, request):
# # #         serializer = self.serializer_class(request.user)
# # #         return Response(serializer.data, status=status.HTTP_200_OK)

# # #     def put(self, request):
# # #         serializer = self.serializer_class(request.user, data=request.data)
# # #         if serializer.is_valid():
# # #             response = update_user_profile(request.user, request.data)
# # #             if response['success']:
# # #                 return Response(response, status=status.HTTP_200_OK)
# # #             else:
# # #                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
# # #         else:
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











































































































# # # # from rest_framework import status
# # # # from rest_framework.response import Response
# # # # from rest_framework.views import APIView
# # # # from rest_framework.permissions import AllowAny, IsAuthenticated
# # # # from django.contrib.auth import logout
# # # # from .serializers import (UserRegistrationSerializer, UserAuthenticationSerializer,
# # # #                           EmailVerificationSerializer, PasswordResetSerializer,
# # # #                           UserProfileSerializer)
# # # # from .services import (register_user, authenticate_user, verify_email,
# # # #                        reset_password, update_user_profile)

# # # # class UserRegistrationView(APIView):
# # # #     permission_classes = (AllowAny,)

# # # #     def post(self, request):
# # # #         response = register_user(request.data)
# # # #         if response['success']:
# # # #             return Response(response, status=status.HTTP_201_CREATED)
# # # #         else:
# # # #             return Response(response, status=status.HTTP_400_BAD_REQUEST)

# # # # class UserAuthenticationView(APIView):
# # # #     permission_classes = (AllowAny,)

# # # #     def post(self, request):
# # # #         response = authenticate_user(request.data)
# # # #         if response['success']:
# # # #             return Response(response, status=status.HTTP_200_OK)
# # # #         else:
# # # #             return Response(response, status=status.HTTP_401_UNAUTHORIZED)

# # # # class EmailVerificationView(APIView):
# # # #     permission_classes = (AllowAny,)

# # # #     def post(self, request):
# # # #         response = verify_email(request.data)
# # # #         if response['success']:
# # # #             return Response(response, status=status.HTTP_200_OK)
# # # #         else:
# # # #             return Response(response, status=status.HTTP_400_BAD_REQUEST)

# # # # class PasswordResetView(APIView):
# # # #     permission_classes = (AllowAny,)

# # # #     def post(self, request):
# # # #         response = reset_password(request.data)
# # # #         if response['success']:
# # # #             return Response(response, status=status.HTTP_200_OK)
# # # #         else:
# # # #             return Response(response, status=status.HTTP_400_BAD_REQUEST)

# # # # class UserProfileView(APIView):
# # # #     permission_classes = (IsAuthenticated,)

# # # #     def get(self, request):
# # # #         serializer = UserProfileSerializer(request.user)
# # # #         return Response(serializer.data, status=status.HTTP_200_OK)

# # # #     def put(self, request):
# # # #         response = update_user_profile(request.user, request.data)
# # # #         if response['success']:
# # # #             return Response(response, status=status.HTTP_200_OK)
# # # #         else:
# # # #             return Response(response, status=status.HTTP_400_BAD_REQUEST)













































































































# # # # # from rest_framework import status
# # # # # from rest_framework.response import Response
# # # # # from rest_framework.views import APIView
# # # # # from rest_framework.permissions import AllowAny, IsAuthenticated
# # # # # from rest_framework.authtoken.models import Token
# # # # # from django.contrib.auth import login, logout
# # # # # from .models import CustomUser
# # # # # from .serializers import (UserRegistrationSerializer, UserAuthenticationSerializer,
# # # # #                           EmailVerificationSerializer, PasswordResetSerializer,
# # # # #                           UserProfileSerializer)

# # # # # class UserRegistrationView(APIView):
# # # # #     permission_classes = (AllowAny,)

# # # # #     def post(self, request):
# # # # #         serializer = UserRegistrationSerializer(data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             serializer.save()
# # # # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # # # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # # # class UserAuthenticationView(APIView):
# # # # #     permission_classes = (AllowAny,)

# # # # #     def post(self, request):
# # # # #         serializer = UserAuthenticationSerializer(data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             user = serializer.validated_data['user']
# # # # #             login(request, user)
# # # # #             token, created = Token.objects.get_or_create(user=user)
# # # # #             return Response({'token': token.key}, status=status.HTTP_200_OK)
# # # # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # # # class EmailVerificationView(APIView):
# # # # #     permission_classes = (AllowAny,)

# # # # #     def post(self, request):
# # # # #         serializer = EmailVerificationSerializer(data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             token = serializer.validated_data['token']
# # # # #             # Your email verification logic here
# # # # #             return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
# # # # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # # # class PasswordResetView(APIView):
# # # # #     permission_classes = (AllowAny,)

# # # # #     def post(self, request):
# # # # #         serializer = PasswordResetSerializer(data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             email = serializer.validated_data['email']
# # # # #             # Your password reset logic here
# # # # #             return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
# # # # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # # # class UserProfileView(APIView):
# # # # #     permission_classes = (IsAuthenticated,)

# # # # #     def get(self, request):
# # # # #         serializer = UserProfileSerializer(request.user)
# # # # #         return Response(serializer.data, status=status.HTTP_200_OK)

# # # # #     def put(self, request):
# # # # #         serializer = UserProfileSerializer(request.user, data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             serializer.save()
# # # # #             return Response(serializer.data, status=status.HTTP_200_OK)
# # # # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

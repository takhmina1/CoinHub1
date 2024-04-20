from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from .models import CustomUser
from .serializers import *

def register_user(data):
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User registered successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def authenticate_user(data):
    email = data.get('email')
    password = data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return {'success': True, 'token': token.key}
    else:
        return {'success': False, 'message': 'Incorrect email or password'}

def verify_email(data):
    serializer = EmailVerificationSerializer(data=data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        # Your email verification logic here
        return {'success': True, 'message': 'Email verified successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def reset_password(data):
    serializer = PasswordResetSerializer(data=data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        # Your password reset logic here
        return {'success': True, 'message': 'Password reset email sent'}
    else:
        return {'success': False, 'errors': serializer.errors}

def update_user_profile(user, data):
    serializer = UserProfileSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User profile updated successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def signup_user(request, data):
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User registered successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def advanced_get_request(url: str, timeout: int) -> dict:
    """Get-запрос, c подключенным логгированием и покрытый исключениями"""

    _response = {
        'response': None,
        'error': False,
        'error_message': None
    }

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as error_request:
        logger.error(msg={'Another Error': error_request})
        _response['error'] = True
        _response['error_message'] = error_request
        return _response
    except requests.exceptions.HTTPError as error_http:
        logger.error(msg={'Http Error': error_http})
        _response['error'] = True
        _response['error_message'] = error_http
        return _response
    except requests.exceptions.ConnectionError as error_connection:
        logger.error(msg={'Error Connecting': error_connection})
        _response['error'] = True
        _response['error_message'] = error_connection
        return _response
    except requests.exceptions.Timeout as error_timeout:
        logger.error(msg={'Timeout Error': error_timeout})
        _response['error'] = True
        _response['error_message'] = error_timeout
        return _response

    _response['response'] = response
    return _response













"""
# utils.py
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from .models import CustomUser
from .serializers import *

def register_user(data):
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User registered successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def authenticate_user(data):
    email = data.get('email')
    password = data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return {'success': True, 'token': token.key}
    else:
        return {'success': False, 'message': 'Incorrect email or password'}

def verify_email(data):
    serializer = EmailVerificationSerializer(data=data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        # Your email verification logic here
        return {'success': True, 'message': 'Email verified successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def reset_password(data):
    serializer = PasswordResetSerializer(data=data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        # Your password reset logic here
        return {'success': True, 'message': 'Password reset email sent'}
    else:
        return {'success': False, 'errors': serializer.errors}

def update_user_profile(user, data):
    serializer = UserProfileSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User profile updated successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def signup_user(request, data):
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'User registered successfully'}
    else:
        return {'success': False, 'errors': serializer.errors}

def advanced_get_request(url: str, timeout: int) -> dict:



    _response = {
        'response': None,
        'error': False,
        'error_message': None
    }

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as error_request:
        logger.error(msg={'Another Error': error_request})
        _response['error'] = True
        _response['error_message'] = error_request
        return _response
    except requests.exceptions.HTTPError as error_http:
        logger.error(msg={'Http Error': error_http})
        _response['error'] = True
        _response['error_message'] = error_http
        return _response
    except requests.exceptions.ConnectionError as error_connection:
        logger.error(msg={'Error Connecting': error_connection})
        _response['error'] = True
        _response['error_message'] = error_connection
        return _response
    except requests.exceptions.Timeout as error_timeout:
        logger.error(msg={'Timeout Error': error_timeout})
        _response['error'] = True
        _response['error_message'] = error_timeout
        return _response

    _response['response'] = response
    return _response



"""
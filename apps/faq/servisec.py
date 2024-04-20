from .models import Question, Answer, Referral, BitcoinConfirmation
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

def create_question(user, title, content):
    """
    Создает новый вопрос.

    Args:
        user (User): Пользователь, задающий вопрос.
        title (str): Заголовок вопроса.
        content (str): Содержание вопроса.

    Returns:
        dict: Информация о созданном вопросе в формате JSON.
    """
    question = Question.objects.create(user=user, title=title, content=content)
    return {
        'id': question.id,
        'user': question.user.username,
        'title': question.title,
        'content': question.content,
        'created_at': question.created_at
    }

def create_answer(user, question_id, content):
    """
    Создает новый ответ на вопрос.

    Args:
        user (User): Пользователь, отвечающий на вопрос.
        question_id (int): Идентификатор вопроса, на который отвечают.
        content (str): Содержание ответа.

    Returns:
        dict: Информация о созданном ответе в формате JSON.
    """
    question = Question.objects.get(id=question_id)
    answer = Answer.objects.create(user=user, question=question, content=content)
    return {
        'id': answer.id,
        'user': answer.user.username,
        'question_id': answer.question.id,
        'content': answer.content,
        'created_at': answer.created_at
    }

def create_referral(user, referral_code, referred_by=None):
    """
    Создает новую запись о реферальной программе.

    Args:
        user (User): Пользователь, участвующий в реферальной программе.
        referral_code (str): Уникальный реферальный код пользователя.
        referred_by (User): Пользователь, который пригласил текущего пользователя (по умолчанию None).

    Returns:
        dict: Информация о созданной записи о реферальной программе в формате JSON.
    """
    referral = Referral.objects.create(user=user, referral_code=referral_code, referred_by=referred_by)
    return {
        'id': referral.id,
        'user': referral.user.username,
        'referral_code': referral.referral_code,
        'referred_by': referral.referred_by.username if referral.referred_by else None,
        'created_at': referral.created_at
    }

def update_bitcoin_confirmation(transaction_id, confirmed=False, confirmation_count=0):
    """
    Обновляет данные о подтверждении Bitcoin.

    Args:
        transaction_id (str): Идентификатор транзакции Bitcoin.
        confirmed (bool): Статус подтверждения (по умолчанию False).
        confirmation_count (int): Количество подтверждений (по умолчанию 0).

    Returns:
        dict: Информация об обновленной записи о подтверждении Bitcoin в формате JSON.
    """
    try:
        bitcoin_confirmation = BitcoinConfirmation.objects.get(transaction_id=transaction_id)
        bitcoin_confirmation.confirmed = confirmed
        bitcoin_confirmation.confirmation_count = confirmation_count
        bitcoin_confirmation.save()
        return {
            'transaction_id': bitcoin_confirmation.transaction_id,
            'confirmed': bitcoin_confirmation.confirmed,
            'confirmation_count': bitcoin_confirmation.confirmation_count,
            'created_at': bitcoin_confirmation.created_at
        }
    except BitcoinConfirmation.DoesNotExist:
        raise ValidationError("Bitcoin confirmation with given transaction_id does not exist.")






































# from .models import Question, Answer, Referral, BitcoinConfirmation
# from django.contrib.auth.models import User

# def create_question(user, title, content):
#     """
#     Создает новый вопрос.

#     Args:
#         user (User): Пользователь, задающий вопрос.
#         title (str): Заголовок вопроса.
#         content (str): Содержание вопроса.

#     Returns:
#         Question: Новый созданный вопрос.
#     """
#     question = Question.objects.create(user=user, title=title, content=content)
#     return question

# def create_answer(user, question_id, content):
#     """
#     Создает новый ответ на вопрос.

#     Args:
#         user (User): Пользователь, отвечающий на вопрос.
#         question_id (int): Идентификатор вопроса, на который отвечают.
#         content (str): Содержание ответа.

#     Returns:
#         Answer: Новый созданный ответ.
#     """
#     question = Question.objects.get(id=question_id)
#     answer = Answer.objects.create(user=user, question=question, content=content)
#     return answer

# def create_referral(user, referral_code, referred_by=None):
#     """
#     Создает новую запись о реферальной программе.

#     Args:
#         user (User): Пользователь, участвующий в реферальной программе.
#         referral_code (str): Уникальный реферальный код пользователя.
#         referred_by (User): Пользователь, который пригласил текущего пользователя (по умолчанию None).

#     Returns:
#         Referral: Новая созданная запись о реферальной программе.
#     """
#     referral = Referral.objects.create(user=user, referral_code=referral_code, referred_by=referred_by)
#     return referral

# def update_bitcoin_confirmation(transaction_id, confirmed=False, confirmation_count=0):
#     """
#     Обновляет данные о подтверждении Bitcoin.

#     Args:
#         transaction_id (str): Идентификатор транзакции Bitcoin.
#         confirmed (bool): Статус подтверждения (по умолчанию False).
#         confirmation_count (int): Количество подтверждений (по умолчанию 0).

#     Returns:
#         BitcoinConfirmation: Обновленная запись о подтверждении Bitcoin.
#     """
#     try:
#         bitcoin_confirmation = BitcoinConfirmation.objects.get(transaction_id=transaction_id)
#         bitcoin_confirmation.confirmed = confirmed
#         bitcoin_confirmation.confirmation_count = confirmation_count
#         bitcoin_confirmation.save()
#         return bitcoin_confirmation
#     except BitcoinConfirmation.DoesNotExist:
#         return None

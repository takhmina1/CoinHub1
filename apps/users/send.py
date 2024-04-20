from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string

class UserService:
    @staticmethod
    def send_confirmation_email(user):
        """
        Отправка письма подтверждения по электронной почте
        """
        subject = 'Подтверждение регистрации'
        message = 'Здравствуйте, ' + user.username + '!\n\n'
        message += 'Вы успешно зарегистрированы на нашем сайте. Спасибо за регистрацию!\n\n'
        message += 'С уважением,\nКоманда сайта'
        
        send_mail(subject, strip_tags(message), 'noreply@example.com', [user.email], fail_silently=False)


class UserService:
    @staticmethod
    def log_balance_operation(user, amount, description):
        log_entry = BalanceLog(user=user, amount=amount, description=description, timestamp=timezone.now())
        log_entry.save()

    @staticmethod
    def send_balance_notification(user, message):
        email_message = render_to_string('balance_notification_email.html', {'user': user, 'message': message})
        send_mail(
            'Уведомление о балансе',
            email_message,
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

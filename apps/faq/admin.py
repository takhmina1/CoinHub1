from django.contrib import admin
from .models import Question, Answer, Referral, BitcoinConfirmation

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'created_at')

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('user', 'referral_code', 'referred_by', 'created_at')

@admin.register(BitcoinConfirmation)
class BitcoinConfirmationAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'confirmed', 'confirmation_count', 'created_at')

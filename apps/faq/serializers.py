from rest_framework import serializers
from .models import Question, Answer, Referral, BitcoinConfirmation
from django.contrib.auth.models import User  

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'

class BitcoinConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinConfirmation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserWithReferralsSerializer(serializers.ModelSerializer):
    referrals = ReferralSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'referrals')

class CreateReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('referral_code', 'referred_by')

class UpdateBitcoinConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinConfirmation
        fields = ('confirmed', 'confirmation_count')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Question
from .serializers import QuestionSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class FAQQuestionListView(APIView):
    """
    Получить список вопросов FAQ.
    """
    @swagger_auto_schema(
        operation_id='faq_question_list',
        responses={200: QuestionSerializer(many=True)},
        security=[],
        tags=['FAQ']
    )
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class FAQQuestionDetailView(APIView):
    """
    Получить информацию о конкретном вопросе FAQ.
    """
    @swagger_auto_schema(
        operation_id='faq_question_detail',
        responses={200: QuestionSerializer()},
        security=[],
        tags=['FAQ']
    )
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

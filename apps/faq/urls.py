from django.urls import path
from .views import FAQQuestionListView, FAQQuestionDetailView

urlpatterns = [
    path('faq/questions/', FAQQuestionListView.as_view(), name='faq_question_list'),
    path('faq/questions/<int:question_id>/', FAQQuestionDetailView.as_view(), name='faq_question_detail'),
]

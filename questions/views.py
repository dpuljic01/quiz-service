from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from questions.models import Question, Answer
from questions.serializers import QuestionSerializer, AnswerSerializer
from quizzes.permissions import IsOwnerPermission


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = QuestionSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = AnswerSerializer

from rest_framework import generics

from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user
        serializer.save()


class QuizDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer
        if not instance.topic:
            instance.topic = "General"
        instance.save()
        return instance

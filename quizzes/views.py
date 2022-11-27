from rest_framework import authentication, generics, permissions, mixins

from quizzes.models import Quiz
from quizzes.serializers import QuizSerializer


class QuizListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user
        serializer.save()


class QuizDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer
        if not instance.topic:
            instance.topic = "General"
        instance.save()
        return instance

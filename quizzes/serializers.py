from rest_framework import serializers

from quizzes.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "name",
            "topic",
            "created_at",
            "started_at",
            "finished_at",
        ]

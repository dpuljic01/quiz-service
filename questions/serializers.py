from rest_framework import serializers

from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "question",
            "created_at",
            "updated_at",
            "answered_at",
        ]

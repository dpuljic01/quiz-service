from rest_framework import serializers

from questions.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ["text", "index", "answers"]
        read_only_fields = ["quiz"]

    def create(self, validated_data):
        validated_data["quiz_id"] = self.context["view"].kwargs["pk"]
        return super().create(validated_data)

    def get_answers(self, obj):
        return [
            AnswerSerializer(answer, context=self.context).data
            for answer in obj.answer_set.all()
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields = ["question"]

    def create(self, validated_data):
        validated_data["question_id"] = self.context["view"].kwargs["question_id"]
        return super().create(validated_data)

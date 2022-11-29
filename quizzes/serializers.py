from rest_framework import serializers

from questions.serializers import QuestionSerializer
from quizzes.models import Quiz, QuizProgress, QuizParticipantAnswer


class QuizSerializer(serializers.ModelSerializer):
    invites = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = "__all__"
        read_only_fields = ["owner"]

    def create(self, validated_data):
        validated_data["owner_id"] = self.context["request"].user.email
        return super().create(validated_data)

    def get_progress(self, obj):
        return [
            QuizProgressSerializer(progress, context=self.context).data
            for progress in obj.quizprogress_set.all()
        ]

    def get_questions(self, obj):
        return [
            QuestionSerializer(question, context=self.context).data
            for question in obj.question_set.all()
        ]

    def get_invites(self, obj):
        return [
            QuizProgressSerializer(invite, context=self.context).data
            for invite in obj.quizprogress_set.all()
        ]


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizParticipantAnswer
        fields = "__all__"
        read_only_fields = ["progress"]

    def create(self, validated_data):
        validated_data["progress"] = QuizProgress.objects.get(
            participant_id=self.context["view"].kwargs["participant_id"],
            quiz_id=self.context["view"].kwargs["quiz_id"],
        )
        return super().create(validated_data)


class QuizProgressSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()

    class Meta:
        model = QuizProgress
        fields = "__all__"

    def get_answers(self, obj):
        answers = []
        for answer in obj.answer_set.all():
            serializer = UserAnswerSerializer(answer, context=self.context)
            answers.append(serializer.data)
        return answers

    def get_score(self, obj):
        return f"{obj.answers_correct} of {obj.answers}"

    def get_progress(self, obj):
        return f"{obj.answers} of {obj.quiz.question_set.count()}"


class InvitationSerializer(serializers.Serializer):
    email = serializers.EmailField()

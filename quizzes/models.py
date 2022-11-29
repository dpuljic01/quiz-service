from django.db import models
from django.db.models import Count, Q, UniqueConstraint
from django_extensions.db.models import TimeStampedModel

from service import settings

User = settings.AUTH_USER_MODEL


class ProgressManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        correct_answers = Count(
            "answer_set",
            filter=Q(answer_set__answer__correct=True),
            distinct=True,
        )
        return queryset.annotate(
            answers=Count("answer_set"), answers_correct=correct_answers
        )


class Quiz(TimeStampedModel):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created"]  # newly created quiz comes first
        verbose_name_plural = "Quizzes"
        db_table = "quiz"

    @property
    def in_progress(self):
        return self.started_at and not self.finished_at

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        return self.question_set.all()


class QuizProgress(TimeStampedModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ProgressManager()

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["participant", "quiz"],
                name="uq_participant_quiz",
            )
        ]
        db_table = "quiz_progress"


class QuizParticipantAnswer(TimeStampedModel):
    progress = models.ForeignKey(
        QuizProgress, on_delete=models.CASCADE, related_name="answer_set"
    )
    answer = models.ForeignKey("questions.Answer", on_delete=models.CASCADE)

    class Meta:
        db_table = "quiz_participant_answer"

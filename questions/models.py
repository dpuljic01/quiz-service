from django.db import models

from helpers.models import BaseModel
from quizzes.models import Quiz


class QuestionManager(models.Manager):
    pass


class Question(BaseModel):
    text = models.CharField(max_length=256)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(null=True, blank=True)

    objects = QuestionManager()

    class Meta:
        db_table = "question"

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    def is_answered(self):
        return self.answered_at is not None


class Answer(BaseModel):
    text = models.CharField(max_length=256)
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "answer"

    def __str__(self):
        return f"answer: {self.text}, correct: {self.correct}"

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Question(TimeStampedModel):
    text = models.CharField(max_length=256)
    quiz = models.ForeignKey("quizzes.Quiz", on_delete=models.CASCADE)
    index = models.PositiveIntegerField()

    class Meta:
        db_table = "question"
        ordering = ["index"]

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(TimeStampedModel):
    text = models.CharField(max_length=256)
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    index = models.PositiveIntegerField()

    class Meta:
        db_table = "answer"
        ordering = ["index"]

    def __str__(self):
        return f"answer: {self.text}, correct: {self.correct}"

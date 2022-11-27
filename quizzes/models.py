import datetime

from django.db import models

from helpers.models import BaseModel


class QuizManager(models.Manager):
    pass


class Quiz(BaseModel):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120, null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    objects = QuizManager()

    class Meta:
        ordering = ["-created_at"]  # newly created quiz comes first
        verbose_name_plural = "Quizzes"
        db_table = "quiz"

    @property
    def in_progress(self):
        return self.started_at and not self.finished_at

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        return self.question_set.all()

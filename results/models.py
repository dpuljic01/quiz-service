from django.db import models

from helpers.models import BaseModel


class Result(BaseModel):
    quiz = models.ForeignKey("quizzes.Quiz", on_delete=models.CASCADE)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = "result"

    def __str__(self):
        return str(self.pk)

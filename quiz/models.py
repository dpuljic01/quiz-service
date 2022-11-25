from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-created_at"]  # newly created quiz comes first
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        return self.question_set.all()

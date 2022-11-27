from django.contrib import admin

from quizzes.models import Quiz
from questions.models import Question, Answer


class QuestionAdmin(admin.StackedInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]


# admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)

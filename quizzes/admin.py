from django.contrib import admin

from questions.models import Question
from quizzes.models import Quiz


class QuestionInline(admin.TabularInline):
    extra = 1
    fields = ["text", "index"]
    model = Question


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    search_fields = ["name", "owner"]
    fields = ["name", "topic", "owner"]
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)

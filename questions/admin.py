from django.contrib import admin

from questions.models import Answer, Question


class AnswerAdmin(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerAdmin]


admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)

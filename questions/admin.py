from django.contrib import admin


from questions.models import Question, Answer


class AnswerInline(admin.TabularInline):
    extra = 1
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)

from django.http import JsonResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from quiz.models import Quiz


class QuizListView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "tasks": Quiz.objects.all(),
            },
        )

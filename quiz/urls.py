from django.urls import path

from quiz.views import QuizListView

urlpatterns = [path("quizzes/", QuizListView.as_view())]

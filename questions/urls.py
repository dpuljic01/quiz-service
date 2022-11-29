from django.urls import path

from questions import views

urlpatterns = [
    path(
        "",
        views.QuestionCreateAPIView.as_view(),
        name="question-create",
    ),
    path(
        "<int:question_id>/answers",
        views.AnswerCreateAPIView.as_view(),
        name="answer-create",
    ),
]

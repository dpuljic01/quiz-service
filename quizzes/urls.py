from django.urls import path, include

from quizzes import views

urlpatterns = [
    path("", views.QuizListCreateAPIView.as_view(), name="quiz-list-create"),
    path("<int:pk>/", views.QuizDetailAPIView.as_view(), name="quiz-detail"),
    path("<int:pk>/questions/", include("questions.urls")),
    path(
        "<int:pk>/invite/",
        views.QuizInviteAPIView.as_view(),
        name="quiz-participant-invite",
    ),
    path(
        "participant/<int:participant_id>/submit/<int:quiz_id>/",
        views.QuizProgressDetailAPIView.as_view(),
        name="submit-detail",
    ),
    path(
        "participant/<int:participant_id>/submit/<int:quiz_id>/answers/",
        views.UserAnswerCreateAPIView.as_view(),
        name="participant-answers-list-create",
    ),
]

from django.urls import path

from quizzes import views

urlpatterns = [
    path("", views.QuizListCreateAPIView.as_view()),
    path("<int:pk>/", views.QuizDetailUpdateAPIView.as_view()),
]

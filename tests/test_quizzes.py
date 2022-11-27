from django.test import RequestFactory, TestCase

from quizzes.models import Quiz
from quizzes.views import QuizListCreateAPIView


class QuizTest(TestCase):
    fixtures = ["quizzes.json"]

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_quizzes(self):
        request = self.factory.get("api/v1/quizzes")
        response = QuizListCreateAPIView.as_view()(request)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.status_code, 200)

    def test_create_quiz(self):
        payload = {"name": "Python quiz", "topic": "Computer Science"}
        request = self.factory.post("api/v1/quizzes", data=payload)
        count_before = Quiz.objects.count()
        response = QuizListCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(Quiz.objects.count(), count_before + 1)

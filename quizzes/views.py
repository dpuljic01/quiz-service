from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, filters
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from helpers.enums import UserRole
from questions.models import Answer
from quizzes.models import Quiz, QuizProgress
from quizzes.permissions import (
    IsOwnerPermission,
    QuizPermission,
    IsParticipantPermission,
    IsCreatorPermission,
)
from quizzes.serializers import (
    QuizSerializer,
    InvitationSerializer,
    QuizProgressSerializer,
)
from quizzes.serializers import (
    UserAnswerSerializer,
)


class QuizListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, QuizPermission]
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if hasattr(self.request.user, "owner"):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, QuizPermission]
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset

        queryset = self.queryset
        if hasattr(user, "owner"):
            queryset = queryset.filter(owner=user)
        if hasattr(user, "role") and user.role == UserRole.PARTICIPANT:
            quiz_ids = user.quizprogress_set.values_list("quiz_id", flat=True)
            queryset = queryset.filter(id__in=quiz_ids)
        return queryset


class UserAnswerCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsParticipantPermission]
    serializer_class = UserAnswerSerializer


class QuizProgressDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsParticipantPermission]
    serializer_class = QuizProgressSerializer

    def get_object(self):
        return QuizProgress.objects.get(
            participant_id=self.kwargs["participant_id"],
            quiz_id=self.kwargs["quiz_id"],
        )


class QuizInviteAPIView(generics.CreateAPIView):
    queryset = QuizProgress.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = InvitationSerializer

    def post(self, request, *args, **kwargs):
        quiz = get_object_or_404(Quiz, id=self.kwargs["pk"])
        serializer = InvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        participant_db = User.objects.filter(
            email=serializer.data["email"], role=UserRole.PARTICIPANT.value
        ).first()
        if not participant_db:
            # Ideally we would redirect to register page here, but since I'm out of time I'll just create it manually
            participant_db = User.objects.create_user(
                username="participant",  # this should actually be set by user upon registration
                email=serializer.data["email"],
                role=UserRole.PARTICIPANT.value,
            )

        activity = QuizProgress.objects.create(
            quiz_id=quiz.id,
            participant_id=participant_db.email,
        )
        send_mail(
            subject="Join a Quiz",
            message=f"You've been invited to {quiz.name}.",
            from_email=quiz.owner.email,
            recipient_list=[participant_db.email],
        )
        return Response({"invitation_id": activity.id}, status=status.HTTP_201_CREATED)

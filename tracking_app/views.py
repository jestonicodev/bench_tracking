
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate
import jwt
from datetime import datetime, timedelta

class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT token
        token = self.generate_jwt_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)

    def generate_jwt_token(self, user):
        # Define payload with user information
        payload = {
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time
        }

        # Encode payload with a secret key
        token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
        return token

    @action(methods=['post'], detail=False)
    def verify_token(self, request):
        token = request.data.get('token')

        try:
            # Decode token with the secret key
            payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            return Response({'valid': True}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class LearningSessionViewSet(viewsets.ModelViewSet):
    queryset = LearningSession.objects.all()
    serializer_class = LearningSessionSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class InterviewQuestionViewSet(viewsets.ModelViewSet):
    queryset = InterviewQuestion.objects.all()
    serializer_class = InterviewQuestionSerializer


class PlacementChecklistViewSet(viewsets.ModelViewSet):
    queryset = PlacementChecklist.objects.all()
    serializer_class = PlacementChecklistSerializer


class OLPTrackingViewSet(viewsets.ModelViewSet):
    queryset = OLPTracking.objects.all()
    serializer_class = OLPTrackingSerializer


class BenchHistoryViewSet(viewsets.ModelViewSet):
    queryset = BenchHistory.objects.all()
    serializer_class = BenchHistorySerializer


class ProjectDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProjectDetails.objects.all()
    serializer_class = ProjectDetailsSerializer


class UpdateReportViewSet(viewsets.ModelViewSet):
    queryset = UpdateReport.objects.all()
    serializer_class = UpdateReportSerializer

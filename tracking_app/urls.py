
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pages', PageViewSet)
router.register(r'learning_sessions', LearningSessionViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'team_members', TeamMemberViewSet)
router.register(r'interview_questions', InterviewQuestionViewSet)
router.register(r'placement_checklists', PlacementChecklistViewSet)
router.register(r'olp_trackings', OLPTrackingViewSet)
router.register(r'bench_histories', BenchHistoryViewSet)
router.register(r'project_details', ProjectDetailsViewSet)
router.register(r'update_reports', UpdateReportViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
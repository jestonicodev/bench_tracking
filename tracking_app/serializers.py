from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_supervisor', 'is_bench_member', 'employee_id', 'temporary_password', 'bench_start_date', 'bench_end_date']


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class LearningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSession
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = '__all__'


class PlacementChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementChecklist
        fields = '__all__'


class OLPTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OLPTracking
        fields = '__all__'


class BenchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchHistory
        fields = '__all__'


class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        fields = '__all__'


class UpdateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateReport
        fields = '__all__'

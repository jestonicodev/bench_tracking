from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.utils.translation import gettext_lazy as _
class User(AbstractUser):
    is_supervisor = models.BooleanField(default=False)
    is_bench_member = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=20, unique=True, null=True)
    temporary_password = models.CharField(max_length=100, blank=True, null=True)
    bench_start_date = models.DateField(null=True)
    bench_end_date = models.DateField(null=True)


    def is_on_bench(self):
        return self.is_bench_member and self.bench_start_date is not None and self.bench_end_date is None


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('Groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. '
            'A user will get all permissions granted to each of their groups.'
        ),
        related_name='tracking_app_users',
        related_query_name='tracking_app_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('User permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='tracking_app_users_permissions',
        related_query_name='tracking_app_user_permission',
    )

    def __str__(self):
        return self.username




class Page(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()


class LearningSession(models.Model):
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    post_training_survey_link = models.URLField()
    post_training_quiz_link = models.URLField()
    session_date = models.DateField()


class Attendance(models.Model):
    session = models.ForeignKey(LearningSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_joined = models.DateTimeField(auto_now_add=True)
    post_training_survey_completion_date = models.DateField(blank=True, null=True)
    post_training_quiz_completion_date = models.DateField(blank=True, null=True)
    post_training_quiz_score = models.FloatField(blank=True, null=True)
    report_date_on_practical_application = models.DateField(blank=True, null=True)
    notes_remarks = models.TextField(blank=True, null=True)


class Team(models.Model):
    name = models.CharField(max_length=100)


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class InterviewQuestion(models.Model):
    category_choices = [
        ('tech', 'Technical'),
        ('work', 'Work-related')
    ]
    category = models.CharField(max_length=10, choices=category_choices)
    question = models.TextField()


class PlacementChecklist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class OLPTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BenchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_date = models.DateField(auto_now_add=True)
    left_date = models.DateField(blank=True, null=True)


class ProjectDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UpdateReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

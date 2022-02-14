from re import T
from statistics import mode
from django.db import models
from django.utils import timezone

# Create your models here.
class Langauge(models.Model):
    langauge = models.CharField(max_length=20)

    def __str__(self):
        return self.langauge


class UserInfo(models.Model):
    GEN = (
        ("male", "MALE"),
        ("female", "FEMALE"),
        ("other", "OTHER"),
    )
    PRO = (
        ("developer", "DEVELOPER"),
        ("project_manager", "PROJECT_MANAGER"),
        ("bussiness_development", "BUSSINESS_DEVELOPMENT"),
        ("qa", "QA"),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GEN)
    profile = models.CharField(max_length=50, choices=PRO)

    def __str__(self):
        return self.name


class ProjectInfo(models.Model):
    project_name = models.CharField(max_length=50)
    project_hier_date = models.DateField(default=timezone.now)
    project_submit_date = models.DateField(blank=True,null=True)
    team_member = models.IntegerField()

    def __str__(self):
        return self.project_name


class GitUserDetails(models.Model):
    git_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    project_langauge = models.ManyToManyField(Langauge)

    def all_project_langauge(self):
        return ",".join([str(p) for p in self.project_langauge.all()])

    def __str__(self):
        return self.user.name #+ "-" + self.project.project_name

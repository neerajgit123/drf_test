from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(GitUserDetails)
class GitUserDetailsAdmin(admin.ModelAdmin):
    list_display = ['git_url','user','project','all_project_langauge']

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','gender','profile']



@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ['project_name','project_hier_date','project_submit_date','team_member']


admin.site.register(Langauge)
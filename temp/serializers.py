from rest_framework import serializers
from .models import *


class LangaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langauge
        fields = ['langauge']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'



class GitUserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = GitUserDetails
        fields = "__all__"




class GitUserDetailSerializers1(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.name')
    project=serializers.ReadOnlyField(source='project.project_name')
    project_langauge=LangaugeSerializer(many=True)
    class Meta:
        model = GitUserDetails
        fields = ['id','git_url','created_at','updated_at','user','project','project_langauge']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = UserInfo.objects.get(pk=instance.user_id).name
        data["project"] = ProjectInfo.objects.get(pk=instance.project_id).project_name
       
        return data
    
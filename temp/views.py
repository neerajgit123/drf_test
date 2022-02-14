import imp
from django.shortcuts import render
from .models import *

# Create your views here.
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

class LangaugeListCreat(ListCreateAPIView):
    queryset=Langauge.objects.all()
    serializer_class=LangaugeSerializer


class UserInfoListCreat(ListCreateAPIView):
    queryset=UserInfo.objects.all()
    serializer_class=UserInfoSerializer

class ProjectInfoListCreat(ListCreateAPIView):
    queryset=ProjectInfo.objects.all()
    serializer_class=ProjectInfoSerializer

class GitUserDetailsInfo(APIView):
    def get(self, request):
        data = GitUserDetails.objects.all()
        serializer = GitUserDetailSerializers1(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GitUserDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView


class GitUserDetailsList_create(ListCreateAPIView):
    queryset = GitUserDetails.objects.all()
    serializer_class = GitUserDetailSerializers

from rest_framework.permissions import IsAuthenticated

class GitUserDetailscrud(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GitUserDetails.objects.all()
    serializer_class = GitUserDetailSerializers
    

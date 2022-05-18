from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def home(requests):
    context = {
        "View_all_Tasks/Create_Task":"http://127.0.0.1:8000/view_or_create",
        "Update/Destroy_Task":"http://127.0.0.1:8000/update_or_delete/1",
    }
    return Response(context)


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


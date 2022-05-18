from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name = "All_available_API's"),
    path('view_or_create',TaskView.as_view(),name = "View_Tasks"),
    path('update_or_delete/<int:pk>',UpdateDeleteTask.as_view(),name = "View_Tasks"),
]
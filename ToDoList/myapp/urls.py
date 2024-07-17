from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('removeTask/<int:task_id>/',views.removeTask,name='removeTask'),
]

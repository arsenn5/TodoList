from django.urls import path

from Todo import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:id>/', views.TaskDetailView.as_view(), name='tasks'),
]

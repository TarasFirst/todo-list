from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView, CompleteTaskView, UndoTaskView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/add/", TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/complete/", CompleteTaskView.as_view(), name="task_complete"),
    path("task/<int:pk>/undo/", UndoTaskView.as_view(), name="task_undo"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tag/add/", TagCreateView.as_view(), name="tag_add"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todo"

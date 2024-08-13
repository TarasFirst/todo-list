from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
    View,
)
from todo.models import Task, Tag
from todo.forms import TaskForm, TagForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]  # Order by not done first, then by newest


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:home")


class TagListView(ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"
    success_url = reverse_lazy("todo:tags")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"
    success_url = reverse_lazy("todo:tags")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("todo:home")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tags")


class CompleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = True
        task.save()
        return redirect("todo:home")


class UndoTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect("todo:home")

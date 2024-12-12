import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, TaskForm
from .models import Task

# APA Reference:
# Kizza, J. M. (2013). Guide to computer network security (3rd ed.). Springer.
#
# API Reference:
# Quotable API: https://api.quotable.io/random

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(created_by=request.user)
    # Disable SSL verification for the API call
    try:
        response = requests.get("https://api.quotable.io/random", verify=False)
        if response.status_code == 200:
            quote_data = response.json()
            quote = quote_data.get("content", "No quote available.")
            author = quote_data.get("author", "Unknown")
        else:
            quote = "No quote available."
            author = "Unknown"
    except requests.exceptions.RequestException:
        # In case of a network error or SSL issue, fallback gracefully
        quote = "No quote available."
        author = "Unknown"

    return render(request, 'task_list.html', {'tasks': tasks, 'quote': quote, 'author': author})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})


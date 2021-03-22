from django.shortcuts import render, redirect
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from django.shortcuts import get_object_or_404

from .forms import SetupForm, EditForm
from django.utils import timezone


def register_task(request):
    if request.method == 'POST':
        form = SetupForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.name = request.POST['name']
            new_task.task = request.POST['regtask']
            status = request.POST['enabled']
            new_task.enabled = True if status == 'on' else False
            interval = request.POST['interval']
            new_task.interval = IntervalSchedule.objects.get(id=interval)
            new_task.start_time = timezone.now()
            new_task.save()
            return redirect('task_list')
    else:
        form = SetupForm()
        return render(request, 'test.html', {'form': form})


def task_list(request):
    tasks = PeriodicTask.objects.select_related('interval').all()
    context = {'tasks': tasks}
    return render(request, 'list_test.html', context)


def edit_task(request, task_id):
    # Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.
    task = get_object_or_404(PeriodicTask, id=task_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=task)
        interval = request.POST['interval']
        form.interval = IntervalSchedule.objects.get(id=interval)
        form.save()
        return redirect('task_list')

    form = EditForm(instance=task)
    return render(request, 'edit_test.html', {'form': form})


def result(request):
    return render(request, 'tasks.html', {})

    # print(datetime.datetime.now())

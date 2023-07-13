from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from todoapp.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model = Task
    template_name = 'listview.html'
    context_object_name = 'task'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'i'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'i'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')

# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "index.html", {'task': task1})


def delete(requset, taskid):
    if requset.method == 'POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(requset, "delete.html")


def update(requset, id):
    task = Task.objects.get(id=id)
    f = TodoForm(requset.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(requset, "edit.html", {'f': f, 'task': task})

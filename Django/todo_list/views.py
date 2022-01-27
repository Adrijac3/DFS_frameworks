from http.client import HTTPResponse
from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

# Create your views here.

def todoView(request):
    all_items = TodoListItem.objects.all()
    return render(request,'todo.html', {'all_items': all_items})

def addTodoView(request):
    # return HttpResponse('hello')
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todo_list/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo_list/')
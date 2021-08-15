from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import TodoList , TodoItem
from django.template import context, loader

# Create your views here.
def index(request) :
    todolists = TodoList.objects.all()
    # items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists' : todolists ,
        # 'todoitems' : items
    }
    
    return render(request , 'todo/index.html' , context)

def detail(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("this list does not exist")

    # todolist = TodoList.objects.get(id= list_id)
    items_list = TodoItem.objects.filter(todo_list = todolist)
    context = {
        'todolists' : todolist ,
        'items_list' : items_list
    }
    return render(request, 'todo/detail.html' , context)

def create(request):
    if request.method =='GET':
        return render(request, 'todo/createlist.html')

    name = request.POST.get('name', None)
    if(name is not None):
        TodoList.objects.create(list_name = name)
    else:
        raise Http404("List name cannot be empty")

    lists = TodoList.objects.all()
    context = {
        'todolists' : lists ,
    }
    return redirect('/todo/')

def update(request,list_id,title):
    try:
        lists = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("this list does not exist")
    lists = TodoList.objects.get(id = list_id)
    # item = TodoItem.objects.get(todo_list = lists)
    context = {
        'todolists' : lists ,

    }
    if request.method =='GET':
        return render(request, 'todo/update.html', context)

    new_title = request.POST.get('title' , None)
    date = request.POST.get('date',None )
    check = request.POST.get('checked' , False)
    if check=='on' :
        check = True
    if(new_title and date is not None):
        if(TodoItem.objects.filter(todo_list = lists, title= title)) :
            TodoItem.objects.filter(todo_list = lists, title= title).update(title = new_title, due_date= date, checked= check )
        else:
            TodoItem.objects.create(todo_list = lists , title = new_title, due_date= date, checked= check )
    else:
        raise Http404("invalid title and date")

    return redirect('/todo/')


def delete(request, list_id):
    try:
        temp = TodoList.objects.filter(id= list_id)
    except TodoList.DoesNotExist:
        raise Http404("this list does not exist")
    temp.delete()
    return redirect('/todo/')

def deleteitem(request,list_id,title):
    try:
        lists = TodoList.objects.get(id = list_id)
        item = TodoItem.objects.get(todo_list = lists, title= title)
    except:
        raise Http404("this item does not exist")
    
    item.delete()
    return redirect('/todo/')

def listname(request, list_id):
    if request.method =='GET':
        return render(request, 'todo/listname.html')

    try:
        lists = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("this list does not exist")
    name = request.POST.get('name', None)
    if(name is not None):
        lists.update(list_name = name)
    else:
        raise Http404("List name cannot be empty")
    
    return redirect('/todo/')
    






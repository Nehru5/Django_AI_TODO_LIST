from django.shortcuts import render,redirect
from todoapp.models import Todo

def add_todo(request):
  if request.method=="POST":
    title = request.POST.get("a")
    Todo.objects.create(title=title)
    return redirect("add_todo_link")
  todos = Todo.objects.all()
  return render(request,"index.html",{"a":todos})
  
def complete_todo(request,id):
  todo = Todo.objects.get(id = id)
  todo.completed = True
  todo.save()
  return redirect("add_todo_link")


def delete_todo(request,id):
  todo = Todo.objects.get(id = id)
  todo.delete()
  return redirect("add_todo_link")
  
    
    
  

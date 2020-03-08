from django.shortcuts import render
from django.utils import timezone
from fApp.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    data = Todo.objects.all().order_by("-added_date")
    dict = {"data":data}
    return render(request,"fApp/index.html",dict)

def fetch(request):
    if request.method == 'GET':
        data = Todo.objects.all().order_by("id")
        data = {"data":data}
        return render(request,"fApp/data.html",data)

def add(request):
    if request.method == 'POST':
        currentDate = timezone.now()
        content = request.POST["content"] 
        # to add data in database
        created_obj = Todo.objects.create(added_date = currentDate, text = content)
        print(request.POST)
        print(currentDate)
        print(content)
        print(created_obj.id)   
    return HttpResponseRedirect("/")

def remove(request,todo_id):
    # to delete data from database
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

    
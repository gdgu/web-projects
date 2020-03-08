from django.shortcuts import render
from .models import Question,Choice

# Create your views here.
def index(request):
    return render(request,"pollster/index.html")

def poll(request):
    if request.method == 'GET':
        data = Question.objects.all().order_by("-id")
        data = {"data":data}
        return render(request,"pollster/polls.html",data)

def choice(request,question_id):
    if request.method == 'GET':
        data = Question.objects.get(id=question_id)
        choices = Choice.objects.all().filter(question_id=question_id)
        context = {"choices":choices, "data":data}
        return render(request,"pollster/choice.html",context)

def result(request,question_id):
    if request.method == 'POST':
        print(request.POST)
        id = int(request.POST["qid"])
        print(type(id))
        v = Choice.objects.get(id=id)
        v.votes+=1
        v.save()
    data = Question.objects.get(id=question_id)
    choices = Choice.objects.all().filter(question_id=question_id).order_by("-votes")
    context = {"choices":choices, "data":data}
    return render(request,"pollster/result.html",context)

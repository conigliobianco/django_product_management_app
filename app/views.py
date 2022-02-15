from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        fname=request.POST['fname']
        student=Student(name=name,fname=fname)
        student.save()
    return render(request, ('index.html'))
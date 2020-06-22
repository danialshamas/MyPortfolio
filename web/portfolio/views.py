from django.shortcuts import render
from . models import Project
# Create your views here.
def home(request):
    danial = Project.objects.all()  # all the data from Model  Project is stored in projects(var) and .all()method use for all the data shown into the page
    return render(request, 'home.html',{'projects': danial})  # In dictionary all the data store in key and the value is variable, next go to home.html
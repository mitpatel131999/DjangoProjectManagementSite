from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser 
from django.contrib  import messages
from . import models

from myapp.models import Project, UserData, ProjectActivity, ProjectDepedency
from myapp.serializers import UserSerializer,ProjectSerializer,ProjectActivitySerializer,ProjectDepedencySerializer

from rest_framework import viewsets

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectActivityViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivity.objects.all()
    serializer_class = ProjectActivitySerializer

class ProjectDepedencyViewSet(viewsets.ModelViewSet):
    queryset = ProjectDepedency.objects.all()
    serializer_class = ProjectDepedencySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
'''
sample data for testing 
'''
data={     'project_id':1,
           'report_date':10,
           'Project_schidule':
        [
        {
        "Task": "A",
        "Dependency":[ ],
        "Scheduled_Duration_Week": 1,
        "Planned_Cost": "700 ",
        "Actual_Complete": 100,
        "Actual_Cost_till_Now": "600 "
        },
        {
        "Task": "B",
        "Dependency": ["A"],
        "Scheduled_Duration_Week": 5,
        "Planned_Cost": "1200 ",
        "Actual_Complete": 20,
        "Actual_Cost_till_Now": "600 "
        },
        {
        "Task": "C",
        "Dependency": ["B"],
        "Scheduled_Duration_Week": 2,
        "Planned_Cost": "1300 ",
        "Actual_Complete": 0,
        "Actual_Cost_till_Now": "0 "
        },
        {
        "Task": "D",
        "Dependency": ["C","F","G"],
        "Scheduled_Duration_Week": 2,
        "Planned_Cost": "1000 ",
        "Actual_Complete": 0,
        "Actual_Cost_till_Now": "0 "
        },
        {
        "Task": "E",
        "Dependency": ["A"],
        "Scheduled_Duration_Week": 2,
        "Planned_Cost": "1000 ",
        "Actual_Complete": 100,
        "Actual_Cost_till_Now": "1000 "
        },
        {
        "Task": "F",
        "Dependency": ["E"],
        "Scheduled_Duration_Week": 3,
        "Planned_Cost": "2100 ",
        "Actual_Complete": 66.67,
        "Actual_Cost_till_Now": "2200 "
        },
        {
        "Task": "G",
        "Dependency": ["A"],
        "Scheduled_Duration_Week": 5,
        "Planned_Cost": "2100 ",
        "Actual_Complete": 100,
        "Actual_Cost_till_Now": "1800 "
        }
        ],
        }
# Create your views here.
def index(request):
    print('mit')
    context={ 'name':'MIT',
              'College':'IIT',
              'CGPA': 9.80,
            }
    return render(request,'index.html', context)

def register(request):
    if request.method == 'POST':
        user = models.User()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.password2 = request.POST['Re-password']
        user.emailId  = request.POST['email']

        if user.password == user.password2:
            if User.objects.filter(email=user.emailId).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            else:
                success=True
        else:
            messages.info(request,'Password Did not matched')
            return redirect('register')
    return render(request,'register.html')

def demo_project(request):



    return render(request,'project.html',data)

def edit_project(request):

    queryset = UserData.objects.all()
    print(queryset)

    return render(request,'edit_project.html',queryset)

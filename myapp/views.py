from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth.models import User 
from django.contrib.auth.models import AnonymousUser 
from django.contrib  import messages , auth
from . import models


from myapp.models import Project, UserData, ProjectActivity, ProjectDepedency
from myapp.serializers import UserSerializer,ProjectSerializer,ProjectActivitySerializer,ProjectDepedencySerializer
from .emailService import sendEmail

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.fields import CurrentUserDefault

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    

class ProjectActivityViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivity.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectActivitySerializer

class ProjectDepedencyViewSet(viewsets.ModelViewSet):
    queryset = ProjectDepedency.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectDepedencySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

'''
Experiment for project scheduling asd their data typr for understanding only no need to mark it hard
'''
TASK = [
			{
				'start': '2018-10-01',
				'end': '2018-10-08',
				'name': 'Redesign website',
				'id': "0",
				'progress': 20
			},
			{
				'start': '2018-10-01',
				'end': '2018-10-08',
				'name': 'Redesign website',
				'id': "1",
				'progress': 20
			},
			{
				'start': '2018-10-03',
				'end': '2018-10-06',
				'name': 'Write new content',
				'id': "1",
				'progress': 5,
				'dependencies': '0,10'
			},
			{
				'start': '2018-10-04',
				'end': '2018-10-08',
				'name': 'Apply new styles',
				'id': "2",
				'progress': 10,
				'dependencies': '1'
			},
			{
				'start': '2018-10-08',
				'end': '2018-10-09',
				'name': 'Review',
				'id': "Task 3",
				'progress': 5,
				'dependencies': '2,1'
			},
			{
				'start': '2018-10-08',
				'end': '2018-10-10',
				'name': 'Deploy',
				'id': "Task 4",
				'progress': 0,
				'dependencies': '2'
			},
			{
				'start': '2018-10-11',
				'end': '2018-10-11',
				'name': 'Go Live!',
				'id': "Task 5",
				'progress': 0,
				'dependencies': 'Task 4',
				'custom_class': 'bar-milestone'
			}
			
		]

'''
Manageing the data upload and load to server and web pages just for  testing front end still need to add data into database and making proper permissions and all.

Needs to add security measure in order to match the security
'''
from django.http import JsonResponse
import json


class USERDATA:
    main_data={
            'activities':[],
            'quotations':[],
            'scheduling':[],
          }
user_main_data=USERDATA()



class UserApi:
    
    def userApiLoadData(request,id):
        print('loading the data',id)
        print(user_main_data.main_data)
        response = {'server_data' : user_main_data.main_data}
        return JsonResponse(response)
    
    def userApiUpLoadData(request,id):

        print('uploading the data',id)
        print(request.method)
        data={}
        if request.method == 'POST':
            ajax_data=request.POST.get('ajax_data')
            print(ajax_data,type(ajax_data))
            ar = json.loads(ajax_data)
            print('ar',ar,type(ar))
            user_main_data.main_data=ar
            print('user_main_data',user_main_data.main_data)
            response = {'server_data' : user_main_data.main_data}
            return JsonResponse(response)
        print(data)
        return JsonResponse(data)

'''
user Activity
'''
class UserActivity:
    # we are only using below function rest of the function are for future use
    def user(request,id):
        return render(request,'user_templates/user_update.html')
    
    def dashboard(request,id):
        return render(request,'user_templates/dashboard.html')
    
    def profile(request,id):
        return render(request,'user_templates/profile.html')
    

class DATA:
    main_data={
            'activities':[],
            'quotations':[],
            'scheduling':[],
          }
main_data=DATA()



class ProjectApi:
    
    def projectApiLoadData(request,id):
        print('loading the data',id)
        print(main_data.main_data)
        response = {'server_data' : main_data.main_data}
        return JsonResponse(response)
    
    def projectApiUpLoadData(request,id):

        print('uploading the data',id)
        print(request.method)
        data={}
        if request.method == 'POST':
            ajax_data=request.POST.get('ajax_data')
            print(ajax_data,type(ajax_data))
            ar = json.loads(ajax_data)
            print('ar',ar,type(ar))
            main_data.main_data=ar
            print('main_data',main_data.main_data)
            response = {'server_data' : main_data.main_data}
            return JsonResponse(response)
        print(data)
        return JsonResponse(data)
        

'''
Successfully manage to send request from web page get server and also able to return it properly 
'''

    
class Project:
    # we are only using below function rest of the function are for future use
    def project(request,id):
        main_data={
            'activities':[],
          }
        send_web={ 'id':id}
        return  render(request,'project_templates/project.html',send_web)
    
    def project_introduction(request,id):
        return  render(request,'project_templates/project_introduction.html')
    
    def planing(request,id):
        return  render(request,'project_templates/planing.html')

    def project_quotation(request,id):
        return  render(request,'project_templates/project_quotation.html')

    def project_report(request,id):
        return  render(request,'project_templates/project_report.html')

    def project_scheduling(request,id):
        return  render(request,'project_templates/project_scheduling.html')

    def project_tracking(request,id):
        return  render(request,'project_templates/project_tracking.html')

    def project_allocation_and_estimate(request,id):
        return  render(request,'project_templates/project_allocation_and_estimation.html')
    
    def project_dashboard(request,id):
        data ={ 'TASK':TASK , 'id':1}
        return  render(request,'project_templates/project_dashboard.html',data)


def demo_user(request,id):
    if request.user.is_authenticated:
        queryset = UserData.objects.filter(id=id)
        print(queryset.values())
        redirect('api/user')
    messages.info(request,'Kindly login')
    redirect('login')

    

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
'''
for Main page of the software
'''
def index(request):
    sign_in=False
    if request.user.is_authenticated:
        sign_in=True
    if request.method == 'POST':
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        sender_subject = request.POST['subject']
        sender_message = request.POST['message']

        if sender_email == '' or sender_name == '' or sender_subject == '' or sender_message == '' :
            context={'mail_send': False,'sign_in':sign_in}
            return render(request,'index.html', context)
            
        message = ' subject :\n'+sender_subject +'\n\n message: \n'+sender_message + '\n\n Name : '+ sender_name + '\n\n email : ' + sender_email
        mail = sendEmail(subject='Product Enquire',message=message,recipient_list=sendEmail.email_target)
        mail.sendEmail()
        context={'mail_send': True ,'sign_in':sign_in}
        return render(request,'index.html', context)



    context={'mail_send': False ,'sign_in':sign_in}
    return render(request,'index.html', context)



'''
user Auth
'''
class UserAuth:
    def register(request):
    
        if request.user.is_authenticated:
            messages.info(request,'Already login')
            redirect('login')
        if request.method == 'POST':
            user = models.UserData()
            user.username = request.POST['username']
            user.password = request.POST['password']
            user.password2 = request.POST['Re-password']
            user.emailId  = request.POST['email']
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.address = request.POST['address']
            if user.password == user.password2:
                print(11)
                if User.objects.filter(username=user.username).exists():
                    print(111)
                    messages.info(request,'Username already used')
                    return redirect('register')
                else:
                    print(2)
                    user_auth=User.objects.create_user(username=request.POST['username'],
                                                    password=request.POST['password'],
                                                    email=request.POST['email'])
                    #user_auth.set_password(request.POST['password'])
                    #user_auth.set_unusable_password()
                    ans = user_auth.save()
                    print(ans,'Mit important')
                    user.save()
                    render(request,'user_auth/login.html')
            else:
                messages.info(request,'Password did not matched')
                return redirect('register')
        return render(request,'user_auth/register.html')

    def login(request):
        if request.user.is_authenticated:
            messages.info(request,'Already login')
            queryset = User.objects.filter(username=request.user).values()
            return redirect('user'+'/'+str(queryset[0]['id']))
            #return redirect('logout')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            queryset = User.objects.filter(username=username).values()
            print(queryset)
            if user is not None:
                auth.login(request,user)
                print('login success')
                return redirect('user'+'/'+str(queryset[0]['id']))
            else:
                messages.info(request,'username or password is incorrect')
                return redirect('login')
            '''
            queryset = UserData.objects.filter(username=user.username).values()
            if len(queryset) < 0:
                messages.info(request,'Username not exist')
                return redirect('login')
            if len(queryset) > 1:
                messages.info(request,'Username user multiple time')
                return redirect('login')
            if len(queryset) == 1:
                user.password2=queryset[0]['password']
                if user.password == user.password2:
                    messages.info(request,'Login Successfully')

                    return redirect('home')
                else:
                    messages.info(request,'Login Successfully')
                    return redirect('login')
            '''

            
        return render(request,'user_auth/login.html')
    def logout(request):
        if request.user.is_authenticated:
            auth.logout(request=request)
            return redirect('logout')
        return render(request,'user_auth/logout.html')

    def change_password(request):
        if request.method == 'POST':
            username = request.POST['username']
            current_password = request.POST['currentpassword']
            new_password = request.POST['newpassword']
            
            if request.user.is_authenticated:
                user = UserData.objects.filter(username=username)
                user2 = User.objects.filter(username=username)
                if len(user) == 1:
                    if user[0].password == current_password:
                        user[0].password = new_password
                        user[0].password2 = new_password
                        user[0].save()
                        user2[0].password = new_password
                        user2[0].save()
                        messages.info(request,'password changed successfully, login again')
                        return redirect('login')
                    else:
                        messages.info(request,' current password is incorrect')
                        return redirect('change_password')
            else:
                messages.info(request,'kindly login')
                return redirect('login')
        return render(request,'user_auth/change_password.html')

    def forget_password(request):
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
        return render(request,'user_auth/register.html')



def project(request,id):
    if request.method == 'POST':
        if 'depedency' in request.POST or 'start' in request.POST  :
            
            print('insert')
            print(request.POST['name'])
            print(request.POST['start'])
            print(request.POST['end'])
            print(request.POST['multi-depedency'])
            
            activity ={
                'start': request.POST['start'],
				'end': request.POST['end'],
				'name': request.POST['name'],
				'id': str(len(TASK)),
				'progress': 50,
				'dependencies': request.POST['multi-depedency']
            }
            print(activity)
            TASK.append(activity)
        elif 'activity' in request.POST:
            for i in TASK:
                if i['id'] == request.POST['activity']:
                    TASK.remove(i)
    data ={ 'TASK':TASK , 'id':1}

    return render(request,'chart/gantta.html',data)




def demo_project(request):


    return render(request,'project.html',data)

def edit_project(request):

    queryset = UserData.objects.all()
    print(queryset)

    return render(request,'edit_project.html',queryset)

def edit_user(request):
    if request.user.is_authenticated:
        query = User.objects.filter(username=str(request.user)).values()
        queryset = UserData.objects.filter(username=query[0]['username']).values()
        queryset1 = Project.objects.filter(username=query[0]['id']).values()
        data={
            'user_id' : query[0]['id'],
            'user_data' : queryset,
            'project_data' : queryset1,
        }
        return render(request,'edit_user.html',data)
    return render(request,'user_auth/login.html')

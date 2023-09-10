from django.db import models

# Create your models here.


class adminUser(models.Model):
    username=models.CharField(max_length=20)
    userId=models.CharField(max_length=20)
    emailId=models.EmailField(max_length=20)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)


class UserData(models.Model):
    userId=models.IntegerField().primary_key
    username=models.CharField(max_length=20)
    isValidated=False
    emailId=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

class Project(models.Model):
    username=models.ForeignKey(UserData, on_delete=models.CASCADE)
    projectId=models.IntegerField().primary_key
    projectDescription=models.CharField(max_length=2000)
    projectSchedule=[]

class ProjectActivity(models.Model):
    ProjectID=models.ForeignKey(Project, on_delete=models.CASCADE)
    ActivityId=models.IntegerField().primary_key
    ActivityDescription=models.CharField(max_length=2000)
    Task=models.CharField(max_length=200)
    PlannedCost=models.IntegerField()
    Duration=models.IntegerField()
    ActualCost=models.IntegerField()
    Actual_Complete=models.FloatField()

class ProjectDepedency(models.Model):
    DepedencyID=models.IntegerField().primary_key
    FromActivity=models.ForeignKey(ProjectActivity, on_delete=models.CASCADE)
    ToActivity=models.IntegerField(ProjectActivity.ActivityId)



    




    
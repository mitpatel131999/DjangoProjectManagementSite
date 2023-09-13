from rest_framework_json_api import serializers

from myapp.models import Project, UserData, adminUser, ProjectActivity,ProjectDepedency

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ('username', 'emailId', 'password','password2','first_name','last_name','address')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('username','projectName', 'projectDescription')

class ProjectActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectActivity
        fields = ('ProjectID','ActivityDescription', 'Task','Duration','PlannedCost','ActualCost','Actual_Complete')

class ProjectDepedencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectDepedency
        fields = ('DepedencyID','FromActivity', 'ToActivity')
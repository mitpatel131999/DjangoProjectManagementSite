from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'project_activity', views.ProjectActivityViewSet)
router.register(r'project_depedency', views.ProjectDepedencyViewSet)

urlpatterns=[
    
    #''' Non Auth Mode for Website '''
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    
    #''' For User Authencation '''
    path('login',views.UserAuth.login,name='login'),
    path('logout',views.UserAuth.logout,name='logout'),
    path('register/',views.UserAuth.register,name='register'),
    path('change_password',views.UserAuth.change_password,name='change_password'),
    path('forget_password',views.UserAuth.forget_password,name='forget_password'),
    
    #''' For User Specific Activity '''
    path('user/<int:id>',views.UserActivity.user,name='user'),
    path('profile/<int:id>',views.UserActivity.profile,name='user'),
    
    #'''For Project Management'''
    path('project/<int:id>',views.project,name='project'),
    path('project/planing/<int:id>',views.Project.planing,name='planing'),
    path('project/project_quotation/<int:id>',views.Project.project_quotation,name='project_quotation'),
    path('project/project_report/<int:id>',views.Project.project_report,name='project_report'),
    path('project/project_scheduling/<int:id>',views.Project.project_scheduling,name='project_scheduling'),
    path('project/project_tracking/<int:id>',views.Project.project_tracking,name='project_tracking'),
    path('project/resource_allocation_and_estimate/<int:id>',views.Project.project_allocation_and_estimate,name='resource_allocation_and_estimate'),
    
    
    #'''User for Tech demo not part of actual project'''
    path('demo_project',views.demo_project,name='project'),
    path('edit_project',views.edit_project,name='edit_project'),
    path('edit_user',views.edit_user,name='edit_user'),
    

    #'''For API call  reserve for future development'''
    path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

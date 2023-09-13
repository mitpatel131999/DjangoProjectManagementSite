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
    path('index',views.index,name='index'),
    
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('change_password',views.change_password,name='change_password'),
    path('forget_password',views.forget_password,name='forget_password'),
    

    path('project/<int:id>',views.project,name='project'),
    path('demo_project',views.demo_project,name='project'),
    
    path('edit_project',views.edit_project,name='edit_project'),
    path('edit_user',views.edit_user,name='edit_user'),
    
    path('api/', include(router.urls)),
    
    #path('demo_user/<int:id>',views.demo_user,name='demo_user'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

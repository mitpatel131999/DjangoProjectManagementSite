from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'project_activity', views.ProjectActivityViewSet)
router.register(r'project_depedency', views.ProjectDepedencyViewSet)

urlpatterns=[
    #path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('demo_project',views.demo_project,name='project'),
    path('edit_project',views.edit_project,name='edit_project'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
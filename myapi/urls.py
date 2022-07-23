from django.db import router
from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.PostViewSet)

urlpatterns = [
    path('upload/',include(router.urls)),
    
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('home/',views.home,name='home'),
    path('',views.getData)
    
]
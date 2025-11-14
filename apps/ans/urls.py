from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ans'

router = routers.DefaultRouter()
router.register('', views.AnsViewSet, basename='ans')

urlpatterns = [
    path('', include(router.urls) )
]
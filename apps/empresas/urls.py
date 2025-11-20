from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'empresas'

router = routers.DefaultRouter()
router.register('', views.EmpresaViewSet, basename='empresas')

urlpatterns = [
    path('', include(router.urls) )
]

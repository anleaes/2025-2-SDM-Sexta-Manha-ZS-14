from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'atendentes'

router = routers.DefaultRouter()
router.register('', views.AtendenteViewSet, basename='atendentes')

urlpatterns = [
    path('', include(router.urls) )
]
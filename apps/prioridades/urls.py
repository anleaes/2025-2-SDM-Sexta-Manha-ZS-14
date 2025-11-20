from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'prioridades'

router = routers.DefaultRouter()
router.register('', views.PrioridadeViewSet, basename='prioridades')

urlpatterns = [
    path('', include(router.urls) )
]

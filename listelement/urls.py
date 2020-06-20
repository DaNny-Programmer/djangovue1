from django.urls import path
from rest_framework import routers
from .viewsets import ElementViewSet

route = routers.SimpleRouter()
route.register('Element', ElementViewSet)


urlpatterns = route.urls

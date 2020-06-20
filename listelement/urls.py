from django.urls import path
from rest_framework import routers
from .viewsets import ElementViewSet, CategoryViewSet, TypeViewSet

route = routers.SimpleRouter()
route.register('Element', ElementViewSet)
route.register('Category', CategoryViewSet)
route.register('Type', TypeViewSet)


urlpatterns = route.urls

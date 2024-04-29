from django.urls import path, include
from rest_framework import routers
from .views import UserViewset

router = routers.DefaultRouter()
router.register(r'users',UserViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('user/',UserViewset.as_view({'get':'list','post':'update'})),
    path('user/<int:pk>/',UserViewset.as_view({'get':'list'}))
]
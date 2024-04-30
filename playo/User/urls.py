from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, SignupAPI


router = routers.DefaultRouter()
router.register(r'users',UserViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('authentication.urls')),
    path('user/',UserViewset.as_view({'post':'update'})),
    path('signup/',SignupAPI.as_view(),name='signup'),
    # path('user/<int:pk>/',UserViewset.as_view({'get':'list'}))
]
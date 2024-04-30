from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from .models import CustomUser
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from .serializers import SignupSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer
    # permission_classes = [permissions.IsAuthenticated]



class SignupAPI(APIView):
    permission_classes = []

    def post(self,request):
        password = request.POST.get('password',None)
        confirm_password = request.POST.get('confirm_password',None)

        if password == confirm_password:
            serializer = SignupSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            data = serializer.data
            response = status.HTTP_201_CREATED

        else:
            data = ''
            raise ValidationError({'password_mismatch':'Password fields didn not match.'})
        return Response(data,status=response)





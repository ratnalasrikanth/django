from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

        

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password'])

            user = CustomUser.objects.create(email=validated_data['email'],password=password)

        return user


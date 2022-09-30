from cmath import e
from curses.ascii import NUL
from dataclasses import field
from pyexpat import model
from webbrowser import get
from rest_framework import serializers
from .models import Account
# User Serializer
class SignUpSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','phone_number','date_of_birth','profile_picture', 'password']
        extra_kwargs = {'password':{'write_only':True}}



    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data )          
        return user

    def validate(self, validated_data):
        username = validated_data.get('username',None),
        email = validated_data.get('email',None),
        phone_number = validated_data.get('phone_number',None),


        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exist')})
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exist')})
        if Account.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number':('phone number already exist')})
        
        return super().validate(validated_data)



   
   
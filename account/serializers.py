from dataclasses import field
from pyexpat import model
from webbrowser import get
from rest_framework import serializers
from .models import Account
# User Serializer
class SignUpSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(max_length = 50)
    last_name = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 50)
    email = serializers.CharField(max_length = 250)
    phone_number = serializers.IntegerField()
    date_of_birth   = serializers.DateField
    profile_picture = serializers.ImageField()
    password = serializers.CharField(max_length = 50)
    # confirm_password = serializers.CharField(max_length = 50)

    class Meta:
        model = Account
        fields = ('first_name','last_name','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}


    def create(self,validate_data):
        # del validate_data['confirm_password']

        user = Account.objects.create_user(**validate_data)
        
        return user

    # def validate(self,value):

    #     if value.get('password')!=value.get('confirm_password'):
    #         raise serializers.ValidationError("Password does not match")
    #     return value




   
   
from rest_framework import serializers


from django.utils import timezone

from users.models import User

import random





class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)




class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp_code = serializers.CharField(max_length=6)












#class RegisterSerializer(serializers.ModelSerializer):
    #phone_number = serializers.CharField(
        #required=True,
        #validators=[UniqueValidator(queryset=User.objects.all())]  
    #)

    #class Meta:
        #model = User
        #field = ['username', 'phone_number']

    #def create(self, validated_data):
        #user = User.objects.create(
            #username=validated_data['username'],
            #phone_number=validated_data['phone_number']  
        #)
        #user.save()
        #return user
            






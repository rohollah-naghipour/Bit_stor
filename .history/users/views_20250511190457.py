import uuid
import random

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Device

from users.serializers import SendOTPSerializer, VerifyOTPSerializer

class SendOTPView(APIView):
    def post(self, request):
        print(request.data)
        serializer = SendOTPSerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            try:
                user = User.objects.filter(phone_number=phone_number)
                print(user)
                otp_code = str(random.randint(10000, 999999))
            
                # send message (sms or email) ==> otp_code
                cache.set(str(phone_number), otp_code, timeout = 2 * 60) 
                return Response({'code OTP': otp_code}, 
                                status=status.HTTP_200_OK)
            except:
                return Response({'message': 'Not registered yet'}, 
                                status= status.HTTP_403_FORBIDDEN)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp_code = serializer.validated_data['otp_code']

            cached_otp = cache.get(phone_number)
            if cached_otp and cached_otp == otp_code:
                cache.delete(phone_number)
                return Response({'message': 'OTP verified successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
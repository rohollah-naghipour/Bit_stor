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
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            otp_code = str(random.randint(10000, 99999))
            cache.set(str(phone_number), otp_code, timeout = 2 * 60) 

            return Response({'code OTP': otp_code}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp_code = serializer.validated_data['otp_code']
            cache_key = f'otp_{phone_number}'
            cached_otp = cache.get(cache_key)
            if cached_otp and cached_otp == otp_code:
                cache.delete(cache_key)
                return Response({'message': 'OTP verified successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
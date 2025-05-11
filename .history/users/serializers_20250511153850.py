from rest_framework import serializers

from django.utils import timezone

from users.models import User

import random



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'phone_number']







class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Phone number already registered.")
        return phone_number

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        otp = str(random.randint(10000, 99999))
        

        user = User(phone_number=phone_number, username=phone_number) #  اجبار به unique بودن username داریم. میتونیم از شماره تلفن استفاده کنیم
        user.otp = otp
        user.otp_expiry = otp_expiry
        user.save()

        send_otp_sms(phone_number, otp)

        return user

class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField()

    def validate(self, data):
        phone_number = data['phone_number']
        otp = data['otp']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid phone number.")

        if user.otp != otp or user.otp_expiry < timezone.now():
            raise serializers.ValidationError("Invalid OTP.")

        return data
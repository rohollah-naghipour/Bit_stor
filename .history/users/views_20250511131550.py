import uuid
import random

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device


class RegisterView(APIView):
 
    def post(self, request):
        print(request.user)

        phone_number = request.data.get('phone_number')
        username = request.data.get('username')
        email = request.data.get('email')

        if not phone_number and not username:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username 
                                    ,phone_number=phone_number
                                    ,email=email)

        except User.DoesNotExist:
            user = User.objects.create_user(username= username,
                                             phone_number=phone_number,
                                             email=email)


        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)

        # send message (sms or email)
        # cache
        cache.set(str(phone_number), code, 2 *60)
        

        return Response({'code': code})

    


class GetTokenView(APIView):

    def post(self, request):
        
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return(Response(status=status.HTTP_401_UNAUTHORIZED))           
        
        
        cached_code = cache.get(str(phone_number))

        print(cached_code)
        print(code)


        if code != cached_code:
            return Response(status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())

        return Response({'token': token})

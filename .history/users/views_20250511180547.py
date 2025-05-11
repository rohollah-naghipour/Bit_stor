import uuid
import random

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Device
from users.serializers import RegisterSerializer




class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        try:
            user = User.objects.get(phone_number=phone_number)
            cached_code = cache.get(str(phone_number))

            print(cached_code)
            print(code)
              
            if code != cached_code:
                return Response(status=status.HTTP_403_FORBIDDEN)
            token = str(uuid.uuid4())
            return Response({'token': token})

        except User.DoesNotExist:
            return(Response(status=status.HTTP_401_UNAUTHORIZED))           
        

        


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from subscriptions.models import Package
from subscriptions.serializers import PackageSerializer

import uuid
import random



class PackageView(APIView):
    def get(self, request):
        try: 
            packages = Package.objects.get(is_enable = True)
            print(packages)
            serializer = PackageSerializer(packages, many=True)
            if serializer.is_valid:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Package.DoesNotExist:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        



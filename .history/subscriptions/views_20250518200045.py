

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import IsAuthenticated

from subscriptions.models import Package, Subscription
from subscriptions.serializers import PackageSerializer, SubscriptionSerializer

from django.utils import timezone



class PackageView(APIView):
    def get(self, request):
        try: 
            packages = Package.objects.filter(is_enable = True)
            serializer = PackageSerializer(packages, many=True)
            if serializer.is_valid:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Package.DoesNotExist:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        


#class SubscriptionView(APIView):
    #def get(self, request):
        #try:
            #subscription = Subscription.objects.filter(
                #user = request.user,expire_time = timezone.now)
    

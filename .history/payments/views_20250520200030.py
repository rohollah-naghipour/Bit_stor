
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from payments.models import Gateway

from payments.serializers import GatewaySerializer


class GatewayView(APIView):
    def get(self, request):
        gateways = Gateway.objects.filter(is_enable=True)
        serializer = GatewaySerializer(gateways, many=True)
        return Response(serializer.data)

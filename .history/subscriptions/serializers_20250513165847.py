from rest_framework import serializers

from subscriptions.models import Package, Subscription



class PackageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package
        fields = ('title', 'description', 'avatar', 'price', 'duration')


from rest_framework import serializers

from subscriptions.models import Package, Subscription



class PackageSerializer(serializers.ModelSerializer):
    
    class meta:
        Model = Package
        fields = ('title', 'description', 'avatar', 'price', 'duration')


from rest_framework import serializers

from subscriptions.models import package, Subscription



class PackageSerializer(serializers.ModelSerializer):
    
    class Meta:
        Model = package
        fields = ['title', 'description', 'avatar', 'price', 'duration']




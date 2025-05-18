from rest_framework import serializers

from subscriptions.models import Package, Subscription



class PackageSerializer(serializers.ModelSerializer):
    
    class Meta:
        Model = Package
        fields = ['title', 'description', 'avatar', 'price', 'duration']


class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ('package', 'created_time', 'expire_time')
from rest_framework import serializers

from subscriptions.models import Package, Subscription



#class PackageSerializer(serializers.ModelSerializer):
    
    #class Meta:
        #Model = Package
        #fields = ('title', 'description', 'avatar', 'price', 'duration')

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'  # یا لیستی از فیلدهایی که می‌خواهید در سریالایزر نمایش داده شوند
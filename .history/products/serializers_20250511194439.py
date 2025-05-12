from rest_framework import serializers

from products.models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('parent','title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'avatar', 'categories')


    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'url')

    # def get_foo(self, obj):
    #     return 'Hello World'
        
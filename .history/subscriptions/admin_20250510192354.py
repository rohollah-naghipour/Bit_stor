from django.contrib import admin

from .models import Package, Subscription



@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_duration_display', 'price']
    
    def get_duration_display(self, obj):
        return obj.get_duration_display()
    get_duration_display.short_description = 'Duration'




#@admin.register(Package)
#class PackageAdmin(admin.ModelAdmin):
    #list_display = ['title', 'sku', 'is_enable', 'price', 'duration']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'created_time', 'expire_time']

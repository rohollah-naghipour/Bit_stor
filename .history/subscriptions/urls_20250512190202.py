from django.urls import path
from subscriptions.views import PackageView



urlpatterns = [
    path('packages/', PackageView.as_view(), name = 'packages'),

]    
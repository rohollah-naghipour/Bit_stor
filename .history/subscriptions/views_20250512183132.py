from django.shortcuts import render

import uuid
import random

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Device

from users.serializers import SendOTPSerializer, VerifyOTPSerializer


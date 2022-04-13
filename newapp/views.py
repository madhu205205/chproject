# from django.shortcuts import render
#
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employe
from rest_framework.serializers import *

from . Serializers import employeSerializer


class EmployeList(APIView):

    def get(self, request):
        Employe1 = Employe.objects.all()
        serializer = employeSerializer(Employe1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

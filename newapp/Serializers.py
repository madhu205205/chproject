from rest_framework import serializers
from .models import Employe


class employeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        # fields = '_all_'
        fields = ('name', 'father', 'mother', 'email','code','phone','address')
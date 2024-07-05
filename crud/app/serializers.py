from rest_framework import serializers
from .models import Student


class studentserilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','rollno','city']

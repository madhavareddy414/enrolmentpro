from rest_framework import serializers
from register.models import Employee

class EmpSer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all_")
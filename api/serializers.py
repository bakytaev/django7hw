from rest_framework import serializers
from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birth_year = serializers.DateField()
    position = serializers.CharField(source='position.appointment', max_length=128)
    wage = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.birth_date = validated_data.get('birth_date')
        instance.position = validated_data.get('position')
        instance.wage = validated_data.get('wage')
        instance.save()
        return instance

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class Position:
    def __int__(self, appointment, department):
        self.appointment = appointment
        self.department = department


pos1 = Position(appointment='Senior Dealer', department='Treasury')


class PositionSerializer(serializers.Serializer):
    appointment = serializers.CharField(max_length=128)
    department = serializers.CharField(max_length=128)


serializer = PositionSerializer(pos1)

json = JSONRenderer().render(serializer.data)

print('\n')
print(json)

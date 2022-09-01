from django.db import models


class Position(models.Model):
    appointment = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.appointment} - {self.department}'


class Employee(models.Model):
    name = models.CharField(max_length=256)
    birth_year = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    wage = models.IntegerField()

    def __str__(self):
        return self.name

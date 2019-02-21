from django.db import models


# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.state_name}'


class Citizen(models.Model):
    citizen_first_name = models.CharField(max_length=20)
    citizen_last_name = models.CharField(max_length=20)
    citizen_state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.citizen_first_name} {self.citizen_last_name}'

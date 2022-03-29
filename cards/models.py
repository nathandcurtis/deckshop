from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=60)
    set = models.CharField(max_length=60)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " | " + self.set + "-" + str(self.number)

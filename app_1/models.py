from django.db import models

# Create your models here.
class training(models.Model):
    training_name=models.CharField(max_length=25)
    training_provider=models.CharField(max_length=25)
    description = models.TextField()

    def __str__(Self):
        return Self.training_name

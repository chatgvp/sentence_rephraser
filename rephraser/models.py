from django.db import models


class Value(models.Model):
    value = models.CharField(max_length=255, null=True)


class Dog(models.Model):
    good_with_children = models.CharField(max_length=255, null=True)
    good_with_other_dogs = models.CharField(
        max_length=100
    )  # Replace 100 with the desired maximum length for the dog's name

    # Add other fields and methods related to the Dog model if needed

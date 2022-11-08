from django.db import models

class BaseModel (models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Position(BaseModel):
    description = models.CharField(max_length=100)

class Person(BaseModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TypeOfOrganization = [
    (1, 'foundation'),
    (2, 'non-governmental organization'),
    (3, 'local collection'),
]
class Category(models.Model):
    name = models.CharField(max_length=64)

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    type = models.IntegerField(choices=TypeOfOrganization)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
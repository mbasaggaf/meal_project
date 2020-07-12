from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=40)
    Descrption = models.CharField(max_length=200, null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="CompanyCreated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=40)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="NationalityCreated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=40)
    Descrption =  models.CharField(max_length=200,null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="mailCreated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Nationality =models.ForeignKey(Nationality, on_delete=models.CASCADE)
    Meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    day = models.DateField()
    count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="foodCreaeby")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(blank=True, null=True)

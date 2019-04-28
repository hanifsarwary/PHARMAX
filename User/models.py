from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Branch(models.Model):
    employee_count = models.PositiveIntegerField()
    address = models.CharField(max_length=250,unique=True)
    phone = models.CharField(max_length=11,unique=True,validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='phone number must be numeric',
            code='invalid_username'
        )])

    def __str__(self):
        return self.address



class CustomUser(AbstractUser):
    des_choice = (
        ('m','manager'),
        ('s','salesman')

    )
    dob = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=11,blank=True,null=True,validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='phone number must be numeric',
            code='invalid_username'
        )])
    salary = models.FloatField(blank=True,null=True)
    cnic = models.CharField(max_length=13,blank=True,null=True,validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='cnic must be numeric',
            code='invalid_username'
        )])
    bid = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    desgination = models.CharField(choices=des_choice,max_length=20,blank=True,null=True)

    def get_type(self):
        return self.desgination

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Supplier(models.Model):
    name = models.CharField(max_length=50,validators=[
        RegexValidator(
            regex='^[A-Z][a-z]*$',
            message='name must be alphabets',
            code='invalid_username'
        )])
    manu_name = models.CharField(max_length=50,validators=[
        RegexValidator(
            regex='^[A-Z][a-z]*$',
            message='name must be alphabets',
            code='invalid_username'
        )])
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(default="000000000",max_length=11,validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='phone number must be numeric',
            code='invalid_username'
        )])

    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=50,validators=[
        RegexValidator(
            regex='^[A-Z][a-z]*$',
            message='name must be alphabets',
            code='invalid_username'
        )])
    mobile_number = models.CharField(max_length=11,)

    def __str__(self):
        return self.name

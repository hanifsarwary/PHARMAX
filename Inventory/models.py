from django.db import models
from User.models import Supplier,Branch,CustomUser,Customer
# Create your models here.



class Medicine(models.Model):
    choices = (('tab','Tablet'),
               ('syr','Syrup'))
    sid = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,unique=True)
    potency = models.PositiveIntegerField(default=10)
    price = models.FloatField(default=0)
    category = models.CharField(choices=choices,max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'


class Inventory(models.Model):
    med_id = models.ForeignKey(Medicine,on_delete=models.CASCADE,to_field='name')
    branch_id = models.ForeignKey(Branch,on_delete=models.CASCADE)
    packet_count = models.PositiveIntegerField(default=0)
    leaf_count = models.PositiveIntegerField(default=0)
    tablet_count = models.PositiveIntegerField(default=0)
    max_pack_count = models.PositiveIntegerField(default=0)
    max_leaf_count = models.PositiveIntegerField(default=0)
    max_tablet_count = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=40)

    def __str__(self):
        return str(self.branch_id)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Medicine Details'


class Transfer_Request(models.Model):
    choices = (('A','Accepted'),
               ('P','Pending'),
               ('R','Received'))
    branchFromid = models.ForeignKey(Branch,on_delete=models.CASCADE)
    request_date = models.DateTimeField(blank=True,null=True)
    accept_date = models.DateTimeField(blank=True,null=True)
    accepted_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=30,choices=choices)

    class Meta:
        verbose_name = 'Transfer Request'
        verbose_name_plural = 'Transfer Requests'


class Transfer_Request_Details(models.Model):
    transfer_request = models.ForeignKey(Transfer_Request,on_delete=models.CASCADE)
    med = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    packet_count = models.PositiveIntegerField(default=0)
    leaf_count = models.PositiveIntegerField(default=0)
    tablet_count = models.PositiveIntegerField(default=0)


class Bill(models.Model):
    date = models.DateTimeField()
    cid = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Bill_Details(models.Model):
    mid = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    bid = models.ForeignKey(Bill,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()


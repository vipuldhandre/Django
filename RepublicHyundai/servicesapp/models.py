from django.db import models
from taxapp.models import TaxMaster
from vehicleapp.models import VehicleDetails
from inventoryapp.models import ProductInventory,ProductMaster
from datetime import *

class LabourCategory(models.Model):
    lab_cat_id = models.AutoField(primary_key=True)
    lab_cat_name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = "labour_category"

    def __str__(self):
        return self.lab_cat_name

class LabourDetails(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=40)
    lab_mob_no = models.CharField(max_length=20)
    lab_addr = models.TextField()
    lab_pin = models.IntegerField()
    lab_city = models.CharField(max_length=30)
    lab_cat =  models.ManyToManyField(LabourCategory)

    class Meta:
        managed = True
        db_table = "labour_details"

    def __str__(self):
        return self.lab_name

class LabourOperationMaster(models.Model):
    lab_op_id = models.AutoField(primary_key=True)
    lab_op_name = models.CharField(max_length=20)
    lab_op_code = models.CharField(max_length=10)
    lab_op_description = models.TextField()
    lab_op_work_hrs = models.FloatField()           #2
    lab_op_rate = models.FloatField()               #100
    lab_op_charges = models.FloatField()            #200
    lab_tax = models.ForeignKey(TaxMaster,on_delete=models.SET_NULL,null=True)
    labop_lab = models.ManyToManyField(LabourDetails)

    class Meta:
        managed = True
        db_table = "labor_operation_master"

    def __str__(self):
        return self.lab_op_name

class RoWorkType(models.Model):
    ro_work_type_id = models.AutoField(primary_key=True)
    ro_work_type_name = models.CharField(max_length=20)
    ro_work_lab = models.ManyToManyField(LabourDetails)

    class Meta:
        managed = True
        db_table = "ro_work_type"

    def __str__(self):
        return self.ro_work_type_name

class RoStatus(models.Model):
    ro_status_id = models.AutoField(primary_key=True)
    ro_status_name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = "ro_status"

    def __str__(self):
        return self.ro_status_name

class RoDetails(models.Model):
    ro_id = models.AutoField(primary_key=True)
    ro_no = models.CharField(max_length=20)
    ro_mileage = models.FloatField()
    ro_created_by = models.CharField(max_length=30, blank=True, null=True)
    ro_closed_by = models.CharField(max_length=30, blank=True, null=True)
    ro_invoice_no = models.CharField(max_length=30, blank=True, null=True)
    ro_received_date = models.DateField(auto_now_add=False)
    ro_received_time = models.TimeField(blank=True,default=time(0,0))
    ro_open_date = models.DateField(auto_now_add=False)
    ro_open_time = models.TimeField(blank=True,default=time(0,0))
    ro_closed_date = models.DateField(auto_now_add=False)
    ro_closed_time = models.TimeField(blank=True,default=time(0,0))
    ro_promise_date = models.DateField(auto_now_add=False)
    ro_promise_time = models.TimeField(blank=True,default=time(0,0))
    rodetails_status = models.ForeignKey(RoStatus,on_delete=models.SET_NULL,null=True)
    rodetails_vehicle = models.OneToOneField(VehicleDetails,on_delete=models.SET_NULL,null=True)
    rodetails_worktype = models.ManyToManyField(RoWorkType)
    ro_remarks = models.TextField()

    class Meta:
        managed = True
        db_table = "ro_details"

    def __str__(self):
        return self.ro_no

class RoPartDetails(models.Model):
    ro_part_id = models.AutoField(primary_key=True)
    ro_part_quantity = models.IntegerField()
    ropart_prod = models.ManyToManyField(ProductMaster)
    ropart_invent = models.ForeignKey(ProductInventory,on_delete=models.CASCADE)
    ropart_rodetails = models.ManyToManyField(RoDetails)

    class Meta:
        managed = True
        db_table = "ro_part_details"

    def __str__(self):
        return f'{self.ro_part_id}'

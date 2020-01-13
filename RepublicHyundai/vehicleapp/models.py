from django.db import models
from customerapp.models import CustomerDetails  #for veh_cust in VehicleDetails class

class VehicleCategory(models.Model):
    veh_cat_id = models.AutoField(primary_key=True) #veh_cat_id should be auto incremented
    veh_cat_type = models.CharField(max_length=30)

    class Meta:
        managed = True

        db_table = "vehicle_category"   #we want table name as vehicle_category by default django provide name as vehicleapp_vehicle_category
    def __str__(self):
        return self.veh_cat_type

class VehicleModel(models.Model):
    veh_mod_id = models.AutoField(primary_key=True) #veh_mod_id should be auto incremented
    veh_mod_name = models.CharField(max_length=30)
    veh_cat = models.ManyToManyField(VehicleCategory)   #In a VehicleCategory there could be multiple models and via versa.

    class Meta:
        managed = True
        db_table = "vehicle_model"  #we want table name as vehicle_model by default django provide name as vehicleapp_vehicle_model

    def __str__(self):
        return self.veh_mod_name

class VehicleDetails(models.Model):
    veh_id = models.AutoField(primary_key=True)
    veh_name = models.CharField(max_length=30)
    veh_color = models.CharField(max_length=10)
    veh_ident_no = models.CharField(max_length=20)
    veh_reg_no = models.CharField(max_length=20)
    veh_reg_date = models.DateField(auto_now_add=False)
    veh_km = models.IntegerField()
    veh_eng_no = models.CharField(max_length=20)
    veh_chassis_no = models.CharField(max_length=20)
    veh_dealer_name = models.CharField(max_length=30)
    veh_model = models.ForeignKey(VehicleModel,on_delete=models.CASCADE)
    veh_ins_comp_name = models.CharField(max_length=20)
    veh_ins_policy_no = models.CharField(max_length=20)
    veh_ins_code = models.CharField(max_length=20)
    veh_remarks = models.TextField()
    veh_cust = models.ForeignKey(CustomerDetails,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "vehicle_details"

    def __str__(self):
        return self.veh_reg_no

from django.db import models
from taxapp.models import TaxMaster

class ProductMaster(models.Model):
    prod_id = models.AutoField(primary_key=True)    #prod_id should be auto incremented
    prod_code = models.CharField(max_length=15)
    prod_name = models.CharField(max_length=40)
    prod_tag = models.CharField(max_length=40)  #prod_tag is used for barcode etc.
    prod_tax = models.ForeignKey(TaxMaster,on_delete=models.SET_NULL,null= True)   #even tax is deleted for particular product. Product will not be deleted. and to insert null value to table null=True

    class Meta:
        managed = True
        db_table = "product_master" #we want table name as product_master by default django provide name as invetoryapp_product_master

    def __str__(self):
        return self.prod_name
        
class VendorDetails(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_code = models.CharField(max_length=20)
    vendor_comp_name = models.CharField(max_length=40)
    vendor_name = models.CharField(max_length=30)
    vendor_cat = models.CharField(max_length=20)
    vendor_addr = models.TextField()
    vendor_gst_no = models.CharField(max_length=20)
    vendor_mob_no = models.CharField(max_length=15)
    vendor_office_no = models.CharField(max_length=15)
    vendor_email = models.EmailField()
    vendor_pan_no = models.CharField(max_length=20)
    vendor_city = models.CharField(max_length=20)
    vendor_pin = models.IntegerField()
    vendor_state = models.CharField(max_length=30)

    class Meta:
        managed = True  #changes should reflect in database table if managed=True
        db_table = "vendor_details"

    def __str__(self):
        return self.vendor_comp_name

class ProductInventory(models.Model):
    prod_invent_id = models.AutoField(primary_key=True)
    prod_total_quantity = models.IntegerField()
    prod_sold_quantity = models.IntegerField()
    prod_amount_without_tax = models.FloatField()
    prod_stock_remaining = models.IntegerField()
    prod_current_selling_price = models.FloatField()
    invent_prod = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    prod_location = models.CharField(max_length=45)
    prod_dispatch_date = models.DateField(auto_now_add=False)
    prod_received_date = models.DateField(auto_now_add=False)
    invent_vendor = models.ForeignKey(VendorDetails,on_delete=models.SET_NULL,null=True)

    class Meta:
        managed = True
        db_table = "product_inventory"

    def __str__(self):
        return self.invent_prod.prod_name

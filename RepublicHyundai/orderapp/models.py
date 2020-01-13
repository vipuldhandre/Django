from django.db import models
from inventoryapp.models import ProductInventory,ProductMaster,VendorDetails

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=False)
    order_requested_by = models.CharField(max_length=30)
    order_discount_percent = models.FloatField()
    order_total_amount = models.FloatField()
    order_sold_by = models.CharField(max_length=40)
    order_status = models.CharField(max_length=15)
    order_vendor = models.ForeignKey(VendorDetails,on_delete=models.SET_NULL,null=True)

    class Meta:
        managed = True
        db_table = "order"

    def __str__(self):
        return self.order_sold_by

class OrderDetails(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_total_amount = models.FloatField()
    order_prod_quantity = models.IntegerField()
    order_details_status = models.CharField(max_length=20)
    order_invent = models.ManyToManyField(ProductInventory)
    order_prod = models.ForeignKey(ProductMaster,on_delete=models.SET_NULL,null=True)
    orderdetails_order = models.ForeignKey(Order,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "order_details"

    def __str__(self):
        return self.order_details_status

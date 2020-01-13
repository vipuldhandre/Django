from django.db import models

class TaxMaster(models.Model):
    tax_master_id = models.AutoField(primary_key=True)  #tax_master_id should be auto incremented
    tax_hsn = models.CharField(max_length=10)   #for hsn code on different products
    tax_prod_desc = models.TextField()
    tax_prod_name = models.CharField(max_length=30)   #name of product
    tax_cgst = models.FloatField()  #tax_cgst may be in floating value like 2.5
    tax_sgst = models.FloatField()
    tax_igst = models.FloatField()
    tax_lab = models.FloatField()

    class Meta:
        managed = True
        db_table = "tax_master" #we want table name as tax_master by default django provide name as taxapp_tax_master

    def __str__(self):
        return self.tax_prod_name

class FinancialYear(models.Model):
    fin_id = models.AutoField(primary_key=True) #fin_id should be auto incremented
    fin_year = models.CharField(max_length=10)
    fin_date_from = models.DateField(auto_now_add=False)
    fin_date_to = models.DateField(auto_now_add=False)

    class Meta:
        managed = True
        db_table = "financial_year" #we want table name as financial_year by default django provide name as taxapp_financial_year

    def __str__(self):
        return self.fin_year

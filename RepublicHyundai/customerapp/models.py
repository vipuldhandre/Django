from django.db import models

class State(models.Model):
    state_id = models.AutoField(primary_key=True)   #it auto-increment state_id
    state_name = models.CharField(max_length=40)
    state_code = models.CharField(max_length=40)
    state_initials = models.CharField(max_length=40)    #state code can be MH32
    igst = models.PositiveIntegerField() #PositiveIntegerField beacause gst is always positive
    cgst = models.PositiveIntegerField() #PositiveIntegerField beacause gst is always positive
    sgst = models.PositiveIntegerField() #PositiveIntegerField beacause gst is always positive

    class Meta:
        managed = True
        db_table = "state"  #we want table name as state by default django provide name as customerapp_state

    def __str__(self):
        return self.state_name

class District(models.Model):
    dist_id = models.AutoField(primary_key=True)    #it auto-increment dist_id
    dist_name = models.CharField(max_length=40)
    dist_state = models.ForeignKey(State,on_delete=models.CASCADE)  #In a state there are multiple district. If district is deleted its associated state should be deleted.(how to access it (d.dist_state.state_name))

    class Meta:
        managed = True
        db_table = "district"   #we want table name as district by default django provide name as customerapp-district

    def __str__(self):
        return self.dist_name

class City(models.Model):
    city_id = models.AutoField(primary_key=True)    #it auto-increment state_id
    city_name = models.CharField(max_length=40)
    city_dist = models.ForeignKey(District,on_delete=models.CASCADE) #In a state there are multiple district. If city is deleted its associated district should be deleted.(how to access it (c.city_dist.dist_state.state_name))

    class Meta:
        managed = True
        db_table = "city"   #we want table name as city by default django provide name as customerapp-city

    def __str__(self):
        return self.city_name

class CustomerType(models.Model):
    cust_type_id = models.AutoField(primary_key=True)   #it auto-increment cust_type_id
    cust_type_name = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = "customer_type"  #we want table name as customer_type by default django provide name as customerapp_customer_type

    def __str__(self):
        return self.cust_type_name

class CustomerDetails(models.Model):
    cust_id = models.AutoField(primary_key=True)    #it auto-increment cust_id
    cust_name = models.CharField(max_length=40)
    cust_mob = models.CharField(max_length=40)
    cust_dob = models.DateField(auto_now_add=False)
    cust_addr = models.TextField()
    cust_email = models.EmailField()
    cust_created_date = models.DateTimeField(auto_now_add=True)
    cust_type = models.ForeignKey(CustomerType,on_delete=models.CASCADE)
    cust_city = models.ForeignKey(City,on_delete=models.CASCADE)
    cust_pin = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = "customer_details"   #we want table name as customer_details by default django provide name as customerapp_customer_details

    def __str__(self):
        return self.cust_name

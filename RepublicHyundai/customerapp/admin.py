from django.contrib import admin
from customerapp.models import *

admin.site.register(State)  #register model Class State

admin.site.register(District)   #register model Class District

admin.site.register(City)   #register model Class City

admin.site.register(CustomerType) #register model Class CustomerType

admin.site.register(CustomerDetails)    #register model Class CustomerDetails

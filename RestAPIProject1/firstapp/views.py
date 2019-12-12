from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework import status

@api_view(['GET','POST'])
def show_emp(request):
    if request.method == 'GET':
        emp_list = Employee.objects.all()
        serializer = EmployeeSerializer(emp_list,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
# Create your views here.

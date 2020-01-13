from django.urls import path
from app.views import about,emp_data

urlpatterns = [

        path('about/',about),
        path('emp/',emp_data),

    ]

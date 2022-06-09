from django.urls import path
from .views import Addoffice, Addvehicle, Addsalary


urlpatterns = [
    path('office/', Addoffice, name='add-office'),
    path('vehicle/', Addvehicle, name='add-vehicle'),
    path('salary/', Addsalary, name='add-salary'),
]

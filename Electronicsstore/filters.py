import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order 
        #fields = '__all__'
        fields = ['customer' , 'devices' , 'status' ] #(المحددين بس بين اليست)
       # exclude = ['customer' , 'devices' , 'status' ]
        #(هنا بيظهر كل 
        # (fields)
        #ماعدا اللي بين اليست )
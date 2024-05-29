from django.forms import ModelForm
from .models import Order
from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm

#املي بيها البيانات لما يكون عندي طلبيه 
class OrderForm(ModelForm):
    class Meta:
      model = Order  
      fields = "__all__"

class CreateNewUser(UserCreationForm):# paramter  creationform لازم يكون من كلاس 
    class Meta:
      model = User 
      fields = ['username' ,'email' ,'password1' ,'password2']
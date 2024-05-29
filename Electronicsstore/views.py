from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm , CreateNewUser
from .filters import OrderFilter
from  django.forms import inlineformset_factory
from django.contrib import messages
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth import authenticate ,logout
from  django.contrib.auth import  login as myLogin  # هيعمل امبورت ان ل صفحه الوجن وهيتم تسميتها بعدها ب mylogin

def home(request):
    #(بعمل متغير اخزن فيه القيم اللي راجعه من المودل)
    customers= Customer.objects.all()
    orders = Order.objects.all()
    T_orders = orders.count()
    p_orders = orders.filter(status = 'Pending').count()
    D_orders = orders.filter (status = 'Delivered').count()
    In_orders = orders.filter (status = 'In progress').count()
    Out_orders = orders.filter (status = 'Out of order').count()

    context ={'customers':customers ,
              'orders':orders,
              'T_orders':T_orders ,
              'P_orders': p_orders ,
              'D_orders': D_orders ,
              'In_orders':In_orders,
              'Out_orders': Out_orders ,

              }

    return  render(request ,'Electronicsstore/dasboard.html',context)

def customer(request,pK):
     customer = Customer.objects.get(id=pK)
     orders = customer.order_set.all()
     number_order = orders.count()

     searchFilter = OrderFilter(request.GET , queryset = orders)
     orders = searchFilter.qs #(بيظهرلي المطلوب فقط  اي المكتوب ف عمليه البحث)


     context ={'customers':customer ,
              'orders':orders,
              'number_order' : number_order ,
              'myFilter' : searchFilter ,
      }


     return render(request ,'Electronicsstore/customer.html',context )

def devices(request):
    devices = Devices.objects.all()
    return render(request,'Electronicsstore/devices.html' , {'devices': devices})

def profile(request):
    return render(request,'Electronicsstore/profile.html')



#def create (request):
    form = OrderForm()
    if request.method == 'POST':
        #print(request.POST)
        form =OrderForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('/')

    context = {'form' : form }
    return render(request ,'Electronicsstore/my_order_form.html', context )


def create (request,pK):
    OrderFormSet = inlineformset_factory(Customer,Order, fields = ('devices','status') , extra = 8)
    customer = Customer.objects.get(id=pK)
    formset = OrderFormSet (queryset = Order.objects.none()  ,instance = customer )
    #form = OrderForm()
    if request.method == 'POST':
        #print(request.POST)
        #form =OrderForm(request.POST)
         formset = OrderFormSet( request.POST , instance=customer)
         if formset.is_valid():
              formset.save()
              return redirect('/')

    #context = {'form' : form }
    context = {'formset' : formset }

    return render(request ,'Electronicsstore/my_order_form.html', context )


def update (request, pK):
    order =  Order.objects.get(id=pK)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form =OrderForm(request.POST ,instance=order)
        if form.is_valid():
         form.save() # بعد الاستدعاء يحفظها في قاعده البيانات
         return redirect('/')
    context = {'form' : form }
    return render(request ,'Electronicsstore/my_order_form.html', context )


def delete (request, pK):
    order = Order.objects.get(id=pK) 

    if request.method == 'POST':
         order.delete()
         return redirect('/')
    context = {'order' : order}
    return render(request ,'Electronicsstore/delete._form.html', context )


def register (request):
     form = CreateNewUser()
     if request.method == 'POST' :   
       form = CreateNewUser(request.POST)
       if form.is_valid():
         form.save() # بعد الاستدعاء يحفظها في قاعده البيانات
         user = form.cleaned_data.get('username')
         messages.success(request ,user+ 'Create Successfully !')
         return redirect('login')
     context = {'form' : form }
      
         
     return render(request ,'Electronicsstore/register.html', context )


#def userLogin (request):
     if request.method == 'POST' :   
        username= request.POST.get('username')#بيستدعي الباسورد واليوزر نيم
        password = request.POST.get('password') 
        user = authenticate(request ,username=username  ,password=password)
        if user is not None:
           myLogin(request, user)
           return redirect('home')
        else : 
            messages.info(request , 'credentials error')

     context = {}
      
         
     return render(request ,'Electronicsstore/login.html', context )


def userLogin(request):
    if request.method == 'POST' :
         username= request.POST['username']
         password= request.POST['password']
         user = authenticate(request,username=username,password=password)
         if user is not None:
             myLogin(request, user)
             return redirect('/')
         else : 
            messages.info(request , 'credentials error')

       
    return render(request ,'Electronicsstore/login.html' )




def userLogout (request):
     logout(request)
     return redirect('login')


# Mona 
# Mona$0123Mona
# Mona23@gmail.com


from django.urls import path
from . import views
urlpatterns = [
     path('' ,views.home ,name ="home"),
    # path('customer/' , views.customer),
     path("devices/", views.devices , name = "devices"),
     path("profile/", views.profile , name = "profile"),
     path('customer/<str:pK>' , views.customer , name = "customer"), 
    #(<str:PK> معناها وجود اكثر من customer في اليوزر يستدعي اللي عاوزه ب ال دي)
    # path('create/' , views.create , name = "create"),
     path('create/<str:pK>' , views.create , name = "create"),
     path('update/<str:pK>' , views.update , name = "update"),
     path('delete/<str:pK>' , views.delete , name = "delete"),
     path('login' , views.userLogin, name='login'),
      path('register' , views.register , name='register'),
       path('logout' , views.userLogout , name='logout'),
    

   ] 

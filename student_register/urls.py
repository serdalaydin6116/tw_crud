
from django.urls import path
# Create your views here.
from .views import index, student_register_list, student_register_add


urlpatterns = [
    path("",index,name="index"),
    path('list/',student_register_list , name='list'),
    path('add/',student_register_add , name='add'),
  

]

from django.urls import path
# Create your views here.
from .views import index, student_register_list, student_register_add, student_register_update, student_register_delete


urlpatterns = [
    path("",index,name="index"),
    path('list/',student_register_list , name='list'),
    path('add/',student_register_add , name='add'),
    path('update/<int:id>',student_register_update , name='update'),
    path('delete/<int:id>',student_register_delete , name='delete'),
  

]
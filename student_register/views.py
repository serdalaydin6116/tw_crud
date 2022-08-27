from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request,'student_register/index.html')



def student_register_list(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'student_register/student_register_list.html',context)
    

def student_register_add(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
      'form':form  
    }
    return render(request,'student_register/student_register_add.html',context)

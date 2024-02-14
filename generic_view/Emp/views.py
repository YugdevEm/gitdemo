from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import include
from django.contrib.auth import login,logout
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from Emp.models import Employee
from django.urls import reverse_lazy

# Create your views here.

# def sign_up(request):
#     if request.method=="POST":
        
#         username=request.POST.get('uname')
#         Email=request.POST['email']
#         Fname=request.POST.get('fname')
#         Lname=request.POST.get('lname')
#         phn=request.POST.get('ph')
#         password=request.POST.get('pass')

#         user_details=User.objects.create_user(first_name=Fname,email=Email,username=username,password=password,
#         usertype='Student',phone=phn,last_name=Lname)
#         user_details.save()

#         dept=request.POST.get('dpt')
#         plustwomark=request.POST.get('pm')
#         details =stud_user.objects.create(dept=dept,plustwo_mark=plustwomark,user_id=user_details)
#         details.save()
#         return HttpResponse("<script>window.alert('successfully saved')</script>")
#     else:
#         return render(request,'signup.html')    

class EmpCreateView(CreateView):
    model=Employee
    template_name='emp_user.html'
    fields='__all__'
    success_url=reverse_lazy('emp_user_create')

class EmplistView(ListView):
    model=Employee
    template_name='emp_list.html'
    context_object_name='employees'

class EmpDelete(DeleteView):
    model=Employee
    success_url=reverse_lazy('emp_user_list')
    template_name='employee_confirm_delete.html'

class EmpUpdate(UpdateView):
    model=Employee
    template_name='emp_user.html'
    fields='__all__'
    success_url=reverse_lazy('emp_user_list')
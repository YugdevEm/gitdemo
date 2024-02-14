from django.urls import path,include
from Emp.views import *

urlpatterns=[path('create/',EmpCreateView.as_view(),name='emp_user_create'), 
    path('list/',EmplistView.as_view(),name='emp_user_list'),
    path('<int:pk>/del/',EmpDelete.as_view(),name='emp_user_delete'),
    path('<int:pk>/update/',EmpUpdate.as_view(),name='emp_user_update'),]
from django.shortcuts import render

# Create your views here.
from app.models import * 
def display_dept(request):
    QLDO = Dept.objects.all()
    d = {'QLDO':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO = Emp.objects.all()
    d = {'QLEO':QLEO}
    return render(request,'display_emp.html',d)
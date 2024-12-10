from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    student=Student.objects.all()
    return render(request,"first_app/home.html",{'stdnt_data':student})

def delete_student(request,roll):
    std=Student.objects.get(pk= roll).delete()
    print(std)
    return redirect("homepage")
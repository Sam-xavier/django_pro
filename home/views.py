from django.shortcuts import render
from django.http import HttpResponse
from.models import Departments,Doctors
from.forms import BookingForm
# Create your views here.
def index(request):
     person={
          "name":"john",
          "age":30,
          "place":"calidut"
     }

     return render(request,'index.html',)

def about(request):
     numbers = {
          "num":10,
     }
     return render(request,'about.html',)

def booking(request):
     if request.method =="POST":
          form = BookingForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'conformation.html')

     form = BookingForm()
     
     dict_form={
          'form': form
     }
     return render(request,'booking.html',dict_form)

def doctors(request):
     dict_doc={
          'doctors':Doctors.objects.all()
     }
     return render(request,'doctors.html',dict_doc)

def contact(request):
     return render(request,'contact.html')

def department(request):
    dict_dept={
         'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
#   return render(request,'ca2020app/inde.html')

from django.shortcuts import render, HttpResponse
#from faker import Faker
#from .models import Employee
from django.http import HttpResponseRedirect

#fake = Faker()


def home(request):
    context = {}
    return render(request, "inde.html", context)


def randomData(request):
    context = {}
   # Employee.objects.all().delete()
    '''
    for _ in range(0, 30):
        Employee.objects.create(EmployeeID=fake.pyint(), EmployeeName=fake.name(),
                                Contact=fake.phone_number(), Address=fake.address())
        context = {
            'posts': Employee.objects.all()
        }
    '''
    return render(request, "random.html", context)

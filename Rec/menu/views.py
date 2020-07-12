from django.shortcuts import render
# from datetime import date
from datetime import datetime,date
from .models import Food, Company
from django.contrib.auth.decorators import login_required
from .forms import CompanyCreationForm
# Create your views here.


def home(request):
    today = date.today()
    list = Food.objects.filter(day=today)

    # print(list)
    return render(request, 'menu\home.html',context={'foods':list})

def allcompany(request):
    allcustomer = Company.objects.all()
    return render(request, 'menu\company.html',context={'company':allcustomer})

@login_required
def companydetul(request,pk):
    com = Company.objects.filter(pk=pk)
    return render(request, 'menu\company.html',context={'company':com})

@login_required
def newcompany(request):

    new_company = CompanyCreationForm()
    if request.method == 'POST':
        new_company = CompanyCreationForm(request.POST)

        if new_company.is_valid():
            # new_company.save(commit=False)
            new_company.created_by.set(request.user)
            new_company.modified_by.set(request.user)
            # new_company.created_by = request.user
            # new_company.modified_by = request.user
            # # new_company.CompanyCreated_by = request.user
            # # new_company.modified_by = request.user
            # # new_company.created_at = datetime.now()
            # # new_company.modified_at = datetime.now()
            print(new_company.created_by)
            new_company.save()
            return allcompany(request)
    else:
        new_company = CompanyCreationForm()
    return render(request, 'menu\createCompany.html', {
        'form': new_company
    })

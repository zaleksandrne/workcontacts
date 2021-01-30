from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Employee, Communication
from .forms import CompanyForm, EmployeeForm, CommunicationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    companies = Company.objects.all()

    return render(
         request,
         "index.html",
         {"companies": companies}
     )


def new_company(request):
    if request.method != "POST":
        form = CompanyForm()
        return render(request, "new_company.html", {"form": form})
    form = CompanyForm(request.POST)
    if form.is_valid():
        form = CompanyForm(request.POST)
        form.save()
        return redirect("index")
    return render(request, "new_company.html", {"form": form})


def new_employee(request):
    if request.method != "POST":
        form = EmployeeForm()
        return render(request, "new_employee.html", {"form": form})
    form = EmployeeForm(request.POST)
    if form.is_valid():
    
        form = EmployeeForm(request.POST)
        form.save()
        return redirect(reverse((profile), kwargs={"id":form.save().id}))
    return render(request, "new_employee.html", {"form": form})


def company_employees(request, slug):
    company = get_object_or_404(Company, slug=slug)
    employees = company.employees.all()
    return render(
         request,
         "company_employees.html",
         {"employees": employees, "company": company}
     )   


def profile(request, id):
    employee = get_object_or_404(Employee, id=id)
    communications = employee.communications.all()
    if request.method != "POST":
        form = CommunicationForm()
        return render(request, "profile.html", {
            "form": form,
            "employee": employee,
            "communications": communications
            })
    form = CommunicationForm(request.POST)
    if form.is_valid():
        instance = Communication(employee_id=id)
        form = CommunicationForm(request.POST, instance=instance)
        form.save()
        form = CommunicationForm()
        return render(request, "profile.html", {
            "form": form,
            "employee": employee, 
            "communications": communications
            })
    return render(request, "profile.html", {
        "form": form,
        "employee": employee,
        "communications": communications
        })


def delete_communication(request, id):
    get_object_or_404(Communication, id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def delete_employee(request, id):
    get_object_or_404(Employee, id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def delete_company(request, id):
    get_object_or_404(Company, id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

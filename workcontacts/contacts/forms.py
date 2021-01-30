from .models import Company, Employee, Communication
from django.forms import ModelForm


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class CommunicationForm(ModelForm):

    class Meta:
        model = Communication
        fields = ('name', 'value',)




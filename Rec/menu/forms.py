from django import forms
from .models import Company
from django.contrib.auth.models import User

class CompanyCreationForm(forms.ModelForm):
    # created_by = forms.ModelMultipleChoiceField()
    # modified_by = forms.ModelMultipleChoiceField()


    class Meta:
        model = Company
        fields = ['name', 'Descrption', 'link','created_by','modified_by']

        widgets = {'created_by': forms.HiddenInput(),'modified_by':forms.HiddenInput()}

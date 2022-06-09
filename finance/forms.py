from django import forms
from .models import DailyExpenses, VehicleExpenses, SalaryExpenses


class OfficeForm(forms.ModelForm):
    class Meta:
        model = DailyExpenses
        fields = ['date', 'expense', 'description', 'amount']
        widgets = {
            'date': forms.SelectDateWidget,
            'expense': forms.Select(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = VehicleExpenses
        fields = ['date', 'vehicle_number', 'description', 'amount']
        widgets = {
            'date': forms.SelectDateWidget,
            'vehicle_number': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SalaryForm(forms.ModelForm):
    class Meta:
        model = SalaryExpenses
        fields = ['date', 'persons', 'amount']
        widgets = {
            'date': forms.SelectDateWidget,
            'persons': forms.Select(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

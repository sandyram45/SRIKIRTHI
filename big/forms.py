from django import forms
from .models import Location, ShopDetails, Sales, Collections
from django.forms.widgets import SelectDateWidget


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'})
        }


class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopDetails
        fields = ['shop_location', 'name']
        widgets = {
            'shop_location': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class SalesInitialForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['date', 'shop_name', 'no_of_cylinders']
        widgets = {'date': SelectDateWidget}


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget,
            'shop_name': forms.Select(attrs={'class': 'form-control'}),
            'no_of_cylinders': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'no_of_empty': forms.NumberInput(attrs={'class': 'form-control'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collections
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'shop_name': forms.Select(attrs={'class': 'form-control'}),
            'collection_amount': forms.NumberInput(attrs={'class': 'form-control'}),
                   }


# class FunForm(forms.Form):
 #   choice = forms.ChoiceField(choices=[(choice.pk, choice) for choice in ShopDetails.objects.filter(shop_location=2)])


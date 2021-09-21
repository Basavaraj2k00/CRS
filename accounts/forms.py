from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

from realtors.models import Owner
from listings.models import Listing, Contribute


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fileds = "__all__"
        exclude = ['user', 'is_mvp', 'hire_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={"placeholder": "About You..", 'class': 'form-control',"rows": "5",
                    "cols": "50", }),

        }


class ListingForm(ModelForm):
    class Meta:
        model = Contribute
        filed = "__all__"
        exclude = ['is_published', 'list_date']
        

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "map_url": forms.TextInput(attrs={'class': 'form-control'}),
            "city": forms.TextInput(attrs={'class': 'form-control'}),
            "area": forms.TextInput(attrs={'class': 'form-control'}),
            "zipcode": forms.TextInput(attrs={'class': 'form-control'}),
            "type": forms.Select(attrs={'class': 'form-control'}),
            "bedrooms": forms.NumberInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),

            "bathrooms": forms.NumberInput(attrs={'class': 'form-control'}),
            "address": forms.Textarea(
                attrs={
                    "placeholder": "Please provide exact address of your house with house number",
                    "rows": "5",
                    "cols": "50",
                    }),

            
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Please provide description about your house. example. Has pool, is on 2nd floor etc.",
                    "rows": "5",
                    "cols": "50",
                    }),


        }

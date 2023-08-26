from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList

from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta():
        model = ShippingAddress
        fields = [
            'rut', 'line1', 'line2', 'city', 'country', 'reference'
        ]
        labels = {
            'line1': 'dirección',
            'line2': 'dirección',
            'city': 'Comuna',
            'country': 'Region',
            'reference': 'Punto dereferencia'
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['rut'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Rut sin punto con -'
        })

        self.fields['line1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Dirección u Oficina de retiro'
        })

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'continue dirección'
        })

        self.fields['city'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['country'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control'
        })

        
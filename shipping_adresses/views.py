from typing import Any
from django import http
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import HttpResponse

from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import ShippingAddress
from .forms import ShippingAddressForm

class ShippingAddressListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_adresses/shipping_adresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    

class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'shipping_adresses/update.html'
    success_message = 'Direccion Actualizada Exitosa'

    def get_success_url(self):
        return reverse('shipping_adresses:shipping_adresses')


    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')

        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)


class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_adresses/delete.html'
    success_url = reverse_lazy('shipping_adresses:shipping_adresses')


    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_addresses:shipping_addresses')

        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not request.user.has_shipping_address()

        shipping_address.save()

        messages.success(request, 'Dirección creada de manera Exitosa')
        return redirect('shipping_adresses:shipping_adresses')


    return render(request, 'shipping_adresses/create.html', {
        'form':form
    })


@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    if request.user.has_shipping_address():
        request.user.shipping_address.update_default(False)
    
    shipping_address.update_default(True)

    return redirect('shipping_adresses:shipping_adresses')

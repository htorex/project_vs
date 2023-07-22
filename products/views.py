from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

class ProducListView(ListView):

    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['message'] = 'Listado De Productos'

        context['products'] = context['product_list']
        
        return context
    
class ProductDetailView(DetailView):

    model = Product
    template_name = 'products/product.html'

class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filter = Q(tittle__icontains=self.query()) | Q(category__tittle__icontains=self.query())
        return Product.objects.filter(filter)
    
    
    def query(self):
        return self.request.GET.get('q')
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        return context
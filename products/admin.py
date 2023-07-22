from django.contrib import admin

from .models import Product

class ProducAdmin(admin.ModelAdmin):

    fields = ('tittle', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Product, ProducAdmin)

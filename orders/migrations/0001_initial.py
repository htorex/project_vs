# Generated by Django 4.1.5 on 2023-08-10 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0003_alter_cartproducts_created_at_alter_carts_products'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(orders.models.OrderStatus['CREATED'], 'CREATED'), (orders.models.OrderStatus['PAYED'], 'PAYED'), (orders.models.OrderStatus['COMPLETED'], 'COMPLETED'), (orders.models.OrderStatus['CANCELED'], 'CANCELED')], default=orders.models.OrderStatus['CREATED'], max_length=50)),
                ('shipping_total', models.IntegerField(default=4000, max_length=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.carts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
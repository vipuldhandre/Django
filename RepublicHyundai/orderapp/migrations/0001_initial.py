# Generated by Django 2.2.4 on 2019-09-24 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('order_requested_by', models.CharField(max_length=30)),
                ('order_discount_percent', models.FloatField()),
                ('order_total_amount', models.FloatField()),
                ('order_sold_by', models.CharField(max_length=40)),
                ('order_status', models.CharField(max_length=15)),
                ('order_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventoryapp.VendorDetails')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_total_amount', models.FloatField()),
                ('order_prod_quantity', models.IntegerField()),
                ('order_details_status', models.CharField(max_length=20)),
                ('order_invent', models.ManyToManyField(to='inventoryapp.ProductInventory')),
                ('order_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventoryapp.ProductMaster')),
                ('orderdetails_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderapp.Order')),
            ],
            options={
                'db_table': 'order_details',
                'managed': True,
            },
        ),
    ]

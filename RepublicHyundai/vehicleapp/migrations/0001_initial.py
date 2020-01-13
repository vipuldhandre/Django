# Generated by Django 2.2.4 on 2019-09-24 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('veh_cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_cat_type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'vehicle_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('veh_mod_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_mod_name', models.CharField(max_length=30)),
                ('veh_cat', models.ManyToManyField(to='vehicleapp.VehicleCategory')),
            ],
            options={
                'db_table': 'vehicle_model',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('veh_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_name', models.CharField(max_length=30)),
                ('veh_color', models.CharField(max_length=10)),
                ('veh_ident_no', models.CharField(max_length=20)),
                ('veh_reg_no', models.CharField(max_length=20)),
                ('veh_reg_date', models.DateField()),
                ('veh_km', models.IntegerField()),
                ('veh_eng_no', models.CharField(max_length=20)),
                ('veh_chassis_no', models.CharField(max_length=20)),
                ('veh_dealer_name', models.CharField(max_length=30)),
                ('veh_ins_comp_name', models.CharField(max_length=20)),
                ('veh_ins_policy_no', models.CharField(max_length=20)),
                ('veh_ins_code', models.CharField(max_length=20)),
                ('veh_remarks', models.TextField()),
                ('veh_cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerapp.CustomerDetails')),
                ('veh_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicleapp.VehicleModel')),
            ],
            options={
                'db_table': 'vehicle_details',
                'managed': True,
            },
        ),
    ]
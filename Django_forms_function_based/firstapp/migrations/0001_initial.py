# Generated by Django 2.2.4 on 2019-12-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('edes', models.CharField(max_length=30)),
                ('esal', models.FloatField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

# Generated by Django 2.2.6 on 2021-04-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covidHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, max_length=200, null=True)),
                ('person_detail', models.CharField(blank=True, max_length=400, null=True)),
                ('person_mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('hospital', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(choices=[('Uttar Pradesh', 'Uttar Pradesh'), ('Maharastra', 'Maharastra'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Haryana', 'Haryana'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Keral', 'Keral'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Rajasthan', 'Rajasthan'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('West Bengal', 'West Bengal'), ('Uttarakhand', 'Uttarakhand')], max_length=100)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('service', models.CharField(choices=[('Beds', 'Beds'), ('Oxygen', 'Oxygen'), ('Plasma', 'Plasma'), ('Remdesivir', 'Remdesivir')], max_length=100)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=100, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

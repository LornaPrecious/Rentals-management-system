# Generated by Django 5.0.1 on 2024-03-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0002_tenants_emergency_contact_phone_alter_tenants_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentproperty',
            name='property_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='parentproperty',
            name='property_size',
            field=models.CharField(blank=True, help_text='Size of the property in square feet', max_length=250, null=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-04-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0012_remove_tenant_unit_parentproperty_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

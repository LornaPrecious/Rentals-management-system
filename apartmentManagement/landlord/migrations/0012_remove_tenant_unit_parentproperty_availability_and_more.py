# Generated by Django 5.0.1 on 2024-04-12 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0011_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='unit',
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='availability',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='bathrooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='bedrooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='floor_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='rent_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='security_deposit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='unit_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='unit_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='unit_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='parent_property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landlord.parentproperty'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]

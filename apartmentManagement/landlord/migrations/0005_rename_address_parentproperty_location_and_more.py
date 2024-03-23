# Generated by Django 5.0.1 on 2024-03-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0004_alter_parentproperty_building_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parentproperty',
            old_name='address',
            new_name='location',
        ),
        migrations.AddField(
            model_name='parentproperty',
            name='rent_average',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

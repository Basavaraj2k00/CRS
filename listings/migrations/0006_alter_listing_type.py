# Generated by Django 3.2.7 on 2021-09-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('BHK', 'BHK'), ('PG', 'PG'), ('Single Room', 'Single Room')], max_length=200, null=True),
        ),
    ]

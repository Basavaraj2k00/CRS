# Generated by Django 3.2.7 on 2021-09-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

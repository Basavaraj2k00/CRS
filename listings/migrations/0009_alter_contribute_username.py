# Generated by Django 3.2.6 on 2021-09-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_contribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribute',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]

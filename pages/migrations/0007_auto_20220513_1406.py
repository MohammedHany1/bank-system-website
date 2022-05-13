# Generated by Django 3.2.5 on 2022-05-13 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='recieverEmail',
            field=models.EmailField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='senderEmail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
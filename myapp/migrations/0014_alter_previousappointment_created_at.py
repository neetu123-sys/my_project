# Generated by Django 5.1.5 on 2025-03-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_bookappointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previousappointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

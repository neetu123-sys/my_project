# Generated by Django 5.1.5 on 2025-03-20 04:46

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blog_bookappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]

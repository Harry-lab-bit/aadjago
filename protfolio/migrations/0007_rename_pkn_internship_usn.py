# Generated by Django 4.2 on 2024-12-11 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0006_internship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internship',
            old_name='pkn',
            new_name='usn',
        ),
    ]

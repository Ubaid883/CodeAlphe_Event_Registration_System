# Generated by Django 5.2.3 on 2025-06-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_Management_System', '0003_alter_registrationmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

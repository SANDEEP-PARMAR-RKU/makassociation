# Generated by Django 3.0.7 on 2020-07-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_register', '0006_auto_20200713_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='inspection_type',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Other', 'Other'), ('demo', 'dempo')], default=('Online', 'Online'), max_length=256),
        ),
    ]

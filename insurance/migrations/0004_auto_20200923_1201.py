# Generated by Django 3.1.1 on 2020-09-23 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_auto_20200923_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='policybuyer', to='insurance.buyer'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insurance.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='policyseller', to='insurance.seller'),
        ),
    ]

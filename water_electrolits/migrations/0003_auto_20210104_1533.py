# Generated by Django 3.1.5 on 2021-01-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_electrolits', '0002_analizes_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analizes',
            name='BE',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='Glu',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='K',
            field=models.FloatField(default=4.5),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='Urea',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='hct',
            field=models.FloatField(default=0.42),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='pH',
            field=models.FloatField(default=7.4),
        ),
        migrations.AlterField(
            model_name='analizes',
            name='temperature',
            field=models.FloatField(default=36.6),
        ),
        migrations.AlterField(
            model_name='general_information',
            name='mass',
            field=models.FloatField(default=70),
        ),
    ]

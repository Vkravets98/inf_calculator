# Generated by Django 3.1.5 on 2021-02-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_electrolits', '0006_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

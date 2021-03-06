# Generated by Django 3.2.7 on 2021-09-07 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210907_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 13, 37, 57, 597920, tzinfo=utc), help_text='Expiry Date', validators=[inventory.models.expiry_date_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='mfg_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 7, 13, 38, 3, 22516, tzinfo=utc), help_text='Manufacturing Date', validators=[inventory.models.mfg_date_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2.5, help_text='(per piece)', max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='(per piece)', max_digits=20),
        ),
    ]

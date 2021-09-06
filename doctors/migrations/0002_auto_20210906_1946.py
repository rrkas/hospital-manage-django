# Generated by Django 3.2.7 on 2021-09-06 14:16

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import doctors.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='aadhaar',
            field=models.CharField(help_text='Aadhaar Card Number Ex: xxxx xxxx xxxx', max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator('[0-9]{4} [0-9]{4} [0-9]{4}', 'Invalid aadhaar number!')]),
        ),
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='archived_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor_archived_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='date_archived',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='departments.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 6, 14, 15, 59, 178119, tzinfo=utc), validators=[doctors.models.dob_validator], verbose_name='Date of Birth (DOB)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=8),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='patient.jpg', upload_to='patient_pics'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(default=None, help_text='Format: +(1-3) (9-13)', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('\\+(9[976]\\d|8[987530]\\d|6[987]\\d|5[90]\\d|42\\d|3[875]\\d|2[98654321]\\d|9[8543210]|8[6421]\\\n|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1) \\d{1,14}$', 'Invalid format! Format: +(1-3) (9-13)')]),
            preserve_default=False,
        ),
    ]
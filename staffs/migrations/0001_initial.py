# Generated by Django 3.2.7 on 2021-09-05 15:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(help_text='Format: +(1-3) (9-13)', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('\\+(9[976]\\d|8[987530]\\d|6[987]\\d|5[90]\\d|42\\d|3[875]\\d|2[98654321]\\d|9[8543210]|8[6421]\\\n|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1) \\d{1,14}$', 'Invalid format! Format: +(1-3) (9-13)')])),
                ('role', models.CharField(choices=[('super_admin', 'Super Admin'), ('admin', 'Admin'), ('accountant', 'Accountant'), ('user', 'User')], default='user', max_length=20)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2022-01-11 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='accountCharges',
            fields=[
                ('transactionId', models.CharField(max_length=266, primary_key=True, serialize=False)),
                ('accountNo', models.CharField(db_index=True, max_length=266)),
                ('accountName', models.CharField(db_index=True, max_length=266)),
                ('accountType', models.CharField(max_length=266)),
                ('chargeType', models.CharField(max_length=100)),
                ('oldBalance', models.FloatField()),
                ('chargeAmount', models.FloatField()),
                ('newBalance', models.FloatField()),
                ('regDate', models.DateTimeField(auto_now_add=True)),
                ('regBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Account Charges',
            },
        ),
    ]

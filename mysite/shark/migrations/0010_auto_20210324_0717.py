# Generated by Django 3.1.6 on 2021-03-24 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shark', '0009_auto_20210324_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tooth',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

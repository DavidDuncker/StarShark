# Generated by Django 3.1.6 on 2021-03-24 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shark', '0008_auto_20210324_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tooth',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='tooth',
            name='reply_id',
        ),
        migrations.AddField(
            model_name='tooth',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shark.shark'),
        ),
        migrations.AddField(
            model_name='tooth',
            name='main_reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shark.tooth'),
        ),
    ]

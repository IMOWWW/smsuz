# Generated by Django 4.2.8 on 2024-10-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='partinfo',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
    ]

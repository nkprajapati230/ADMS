# Generated by Django 5.1 on 2024-08-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhulkus', '0005_alter_bhulku_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bhulku',
            name='regular',
            field=models.BooleanField(default=False),
        ),
    ]

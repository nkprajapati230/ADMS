# Generated by Django 5.1 on 2024-08-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhulkus', '0007_alter_bhulku_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhulku',
            name='dob',
            field=models.DateField(default='2028-06-05'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]

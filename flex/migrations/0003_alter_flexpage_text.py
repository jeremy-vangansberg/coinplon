# Generated by Django 4.1.2 on 2022-10-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(max_length=600, null=True),
        ),
    ]

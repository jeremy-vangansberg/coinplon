# Generated by Django 4.1.2 on 2022-10-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0013_alter_flexpage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(blank=True, default='Quaerat quiquia est quiquia dolor adipisci magnam. Quaerat quisquam magnam etincidunt sed sit. Porro dolore dolore adipisci dolor. Neque dolor ut adipisci sit dolorem. Voluptatem sit eius sed quaerat.', max_length=600, null=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_alter_flexpage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(default='Numquam labore modi quiquia neque. Quaerat aliquam ipsum voluptatem adipisci. Quiquia modi amet dolorem. Sed sit dolore numquam etincidunt dolorem. Magnam adipisci velit ut numquam non. Quaerat eius consectetur labore magnam.', max_length=600, null=True),
        ),
    ]
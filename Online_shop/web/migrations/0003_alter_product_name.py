# Generated by Django 4.1.4 on 2022-12-23 08:19

import Online_shop.validators.input_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_barcode_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(2), Online_shop.validators.input_validators.validate_only_letters, Online_shop.validators.input_validators.validate_no_special_symbols_include]),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-15 15:28

import Online_shop.validators.input_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.IntegerField(max_length=32, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(32)])),
                ('name', models.IntegerField(max_length=64, validators=[django.core.validators.MinLengthValidator(2), Online_shop.validators.input_validators.validate_only_letters, Online_shop.validators.input_validators.validate_no_special_symbols_include])),
                ('type', models.CharField(choices=[('Vegetable', 'Vegetable'), ('Milk product', 'Milk product'), ('Meat', 'Meat'), ('BIO product', 'BIO product'), ('Non food', 'Non food')], max_length=12)),
                ('category', models.CharField(choices=[('Cheep', 'Cheep'), ('Middle price', 'Middle price'), ('Expensive', 'Expensive')], max_length=12)),
                ('origin', models.CharField(max_length=32, validators=[Online_shop.validators.input_validators.validate_only_letters])),
                ('stock', models.IntegerField(default=50, max_length=1000)),
                ('price', models.IntegerField(max_length=32)),
                ('second_price', models.IntegerField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-15 15:28

import Online_shop.validators.input_validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, validators=[Online_shop.validators.input_validators.validate_no_special_symbols_include])),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('account_type', models.CharField(choices=[('Client', 'Client'), ('Account admin', 'Account admin'), ('Content admin', 'Content admin')], default='Client', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('user_first_name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(2), Online_shop.validators.input_validators.validate_no_special_symbols_include, Online_shop.validators.input_validators.validate_only_letters])),
                ('user_last_name', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.MinLengthValidator(3), Online_shop.validators.input_validators.validate_no_special_symbols_include, Online_shop.validators.input_validators.validate_only_letters])),
                ('user_email', models.EmailField(blank=True, max_length=64, null=True, validators=[django.core.validators.MinLengthValidator(7)])),
                ('user_phone', models.IntegerField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)])),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_acc', serialize=False, to='accounts.user_account')),
            ],
        ),
        migrations.CreateModel(
            name='User_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64, validators=[Online_shop.validators.input_validators.validate_no_special_symbols_include, Online_shop.validators.input_validators.validate_only_letters, django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=64, validators=[Online_shop.validators.input_validators.validate_no_special_symbols_include, Online_shop.validators.input_validators.validate_only_letters, django.core.validators.MinLengthValidator(4)])),
                ('address', models.TextField()),
                ('additional_info', models.TextField(blank=True, max_length=1024, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_profile')),
            ],
        ),
    ]

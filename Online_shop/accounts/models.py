import django.core.validators as django_validators
from django.contrib.auth import models as auth_models
from django.db import models

from Online_shop.accounts.managers import YouCookUserManager
from Online_shop.validators.input_validators import validate_no_special_symbols_include, validate_only_letters


class User_account(auth_models.AbstractUser , auth_models.PermissionsMixin):

    USER_NAME_MAX_LENGTH = 32

    CLIENT = "Client"
    ACCOUNT_ADMIN = "Account admin"
    CONTENT_ADMIN = "Content admin"

    ACCOUNT_TYPES = [(x,x) for x in (CLIENT,ACCOUNT_ADMIN,CONTENT_ADMIN)]

    username = models.CharField(
        unique= True,
        max_length= USER_NAME_MAX_LENGTH,
        validators= (
            validate_no_special_symbols_include,
        )
    )

    join_date = models.DateTimeField(
        auto_now_add=True,
    )

    account_type = models.CharField(

        max_length= max([len(x) for x , _ in ACCOUNT_TYPES]),
        default= CLIENT,
        choices= ACCOUNT_TYPES

    )
    USERNAME_FIELD = 'username'
    objects =  YouCookUserManager




class User_profile(models.Model):

    USER_FIRST_NAME_MAX_LEN = 32
    USER_FIRST_NAME_MIN_LEN = 2
    USER_LAST_NAME_MAX_LEN = 32
    USER_LAST_NAME_MIN_LEN = 3
    USER_EMAIL_MAX_LEN = 64
    USER_EMAIL_MIN_LEN = 7
    USER_PHONE_LEN = 9

    user_first_name = models.CharField(

        max_length=USER_FIRST_NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(USER_FIRST_NAME_MIN_LEN),
            validate_no_special_symbols_include,
            validate_only_letters,
        ),
        blank= False,
        null=False,

    )

    user_last_name = models.CharField(

        max_length=USER_LAST_NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(USER_LAST_NAME_MIN_LEN),
            validate_no_special_symbols_include,
            validate_only_letters,
        ),
        blank=True,
        null=True,

    )

    user_email  = models.EmailField(

        max_length=USER_EMAIL_MAX_LEN,
        validators=(

            django_validators.MinLengthValidator(USER_EMAIL_MIN_LEN),

        ),
        blank=True,
        null=True,

    )

    user_phone = models.IntegerField(

        validators= (


        ),
        blank=False,
        null=False,
    )

    user = models.OneToOneField(

        User_account,
        on_delete=models.CASCADE,
        primary_key= True,
        related_name='profile_acc',

    )



class User_address(models.Model):

    CITY_MAX_LEN = 64
    CITY_MIN_LEN = 4
    ADDITIONAL_INFO_MAX_LEN = 1024

    country = models.CharField(
        max_length=CITY_MAX_LEN,
        validators=(
            validate_no_special_symbols_include,
            validate_only_letters,
            django_validators.MinLengthValidator(CITY_MIN_LEN),
        ),
        blank=False,
        null=False,

    )

    city = models.CharField(
        max_length = CITY_MAX_LEN,
        validators=(
            validate_no_special_symbols_include,
            validate_only_letters,
            django_validators.MinLengthValidator(CITY_MIN_LEN),
        ),
        blank=False,
        null=False,

    )

    address = models.TextField(
        blank=False,
        null=False,
    )

    additional_info = models.TextField(
        max_length= ADDITIONAL_INFO_MAX_LEN,
        blank=True,
        null=True,
    )

    user_profile = models.ForeignKey(

        User_profile,
        on_delete= models.CASCADE,

    )

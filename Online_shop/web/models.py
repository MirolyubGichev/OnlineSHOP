from django.db import models
import django.core.validators as django_validators

from Online_shop.validators.input_validators import validate_only_letters, validate_no_special_symbols_include


class Product(models.Model):

    INPUT_MAX_LEN = 32

    PRODUCT_BARCODE_LEN = 32
    PRODUCT_NAME_MAX_LEN = 64
    PRODUCT_NAME_MIN_LEN = 2


    #PODUCT TYPES
    VEGETABLES = "Vegetable"
    MEAT = "Meat"
    MILK = "Milk product"
    BIO = "BIO product"
    NONFOOD = "Non food"
    PRODUCT_TYPES = [(x,x) for x in (VEGETABLES,MILK,MEAT,BIO,NONFOOD)]

    #PRODUCT CATEGORIES
    CHEAP = "Cheep"
    MIDPRICE = "Middle price"
    EXPENSIVE = "Expensive"
    PRODUCT_CATEGORIES = [(x,x) for x in (CHEAP,MIDPRICE,EXPENSIVE)]

    barcode = models.IntegerField(

        primary_key= True,
        validators=(
        ),
        blank=False,
        null=False,
    )

    name = models.CharField(

        max_length= INPUT_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(PRODUCT_NAME_MIN_LEN),
            validate_only_letters,
            validate_no_special_symbols_include,
        ),
        blank=False,
        null=False,
    )

    type = models.CharField(
        max_length= max([len(x) for x , _ in PRODUCT_TYPES]),
        choices= PRODUCT_TYPES,
        # blank=False,
        # null=False,

    )

    category = models.CharField(
        max_length=max([len(x) for x, _ in PRODUCT_CATEGORIES]),
        choices = PRODUCT_CATEGORIES,
        # blank=False,
        # null=False,
    )

    origin = models.CharField(

        max_length=INPUT_MAX_LEN,
        validators=(
            validate_only_letters,
        ),
        blank=False,
        null=False,


    )

    stock = models.IntegerField(

        default= 50,
        #default= 0
        blank=False,
        null=False,
    )

    price = models.IntegerField(

        blank=False,
        null=False,
    )

    second_price = models.IntegerField(


        blank=True,
        null=True,
    )

    sales = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )

    likes = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )

    promo = models.BooleanField(
        default= False,
        blank=False,
        null=False,
    )


class Product_discount(models.Model):

    WEEKLY = "Weekly"
    SELLOUT = "Sellout"
    CUSTOM = "Custom"




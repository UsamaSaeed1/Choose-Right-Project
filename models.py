# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BrandTable(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_table'


class CatagoryTable(models.Model):
    catagory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'catagory_table'


class StoreTable(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=45, blank=True, null=True)
    brand = models.ForeignKey('BrandTable', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'store_table'


class ProductTable(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255, blank=True, null=True)
    product_review = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    store_link = models.CharField(max_length=500, blank=True, null=True)
    product_specification = models.ForeignKey('ProductSpecificationTable', on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey('StoreTable', on_delete=models.CASCADE, blank=True, null=True)
    catagory = models.ForeignKey('CatagoryTable', on_delete=models.CASCADE, blank=True, null=True)
    search_tags = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_table'


class ProductSpecificationTable(models.Model):
    product_specification_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_brand = models.CharField(max_length=45, blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    colore = models.CharField(max_length=45, blank=True, null=True)
    sim = models.CharField(max_length=45, blank=True, null=True)
    ram = models.CharField(max_length=45, blank=True, null=True)
    storage = models.CharField(max_length=45, blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    multi_tasking = models.CharField(max_length=45, blank=True, null=True)
    processor = models.CharField(max_length=45, blank=True, null=True)
    touch_screen = models.CharField(max_length=45, blank=True, null=True)
    battery = models.CharField(max_length=45, blank=True, null=True)
    product_review = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product = models.ForeignKey('ProductTable', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_specification_table'



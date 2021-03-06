# Generated by Django 3.0.8 on 2020-08-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandTable',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brand_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CatagoryTable',
            fields=[
                ('catagory_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Catagory',
                'verbose_name_plural': 'Catagories',
                'db_table': 'catagory_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSpecificationTable',
            fields=[
                ('product_specification_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_brand', models.CharField(blank=True, max_length=45, null=True)),
                ('release_year', models.TextField(blank=True, null=True)),
                ('colore', models.CharField(blank=True, max_length=45, null=True)),
                ('sim', models.CharField(blank=True, max_length=45, null=True)),
                ('ram', models.CharField(blank=True, max_length=45, null=True)),
                ('storage', models.CharField(blank=True, max_length=45, null=True)),
                ('weight', models.CharField(blank=True, max_length=45, null=True)),
                ('size', models.CharField(blank=True, max_length=45, null=True)),
                ('multi_tasking', models.CharField(blank=True, max_length=45, null=True)),
                ('processor', models.CharField(blank=True, max_length=45, null=True)),
                ('touch_screen', models.CharField(blank=True, max_length=45, null=True)),
                ('battery', models.CharField(blank=True, max_length=45, null=True)),
                ('product_review', models.CharField(blank=True, max_length=255, null=True)),
                ('product_price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'product_specification_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_brand', models.CharField(blank=True, max_length=255, null=True)),
                ('product_review', models.CharField(blank=True, max_length=255, null=True)),
                ('product_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('store_link', models.CharField(blank=True, max_length=500, null=True)),
                ('search_tags', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'product_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoreTable',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('slug', models.SlugField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'db_table': 'store_table',
                'managed': False,
            },
        ),
    ]

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from chooseright.utils import unique_slug_generator
from django.contrib.auth import get_user_model
from django.urls import reverse


class CatagoryTable(models.Model):
    catagory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    slug = models.SlugField(max_length=45, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'catagory_table'
        verbose_name = _("Catagory")
        verbose_name_plural = _("Catagories")

    def __str__(self):
        return self.name

    #Enabling Brand table to access data through foreign key
    def products(self):
            return BrandTable.objects.filter(catagory=self)

    def get_absolute_url(self):
        return reverse('core:catagory', kwargs={'slug_text':self.slug})


class BrandTable(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    catagory = models.ForeignKey('CatagoryTable', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=45, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'brand_table'
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:brand', kwargs={'slug_text':self.slug})


class StoreTable(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    brand = models.ForeignKey(BrandTable, models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(
        default = 'store_pics/store_default.png',
        upload_to = 'store_pics'
        )
    


    class Meta:
        managed = False
        db_table = 'store_table'
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def __str__(self):
        return self.name

    #Handling Image upload and delete 
    def save(self, *args, **kwargs):
        try:
            this = StoreTable.objects.get(store_id=self.store_id)
            if this.image != self.image:
                if this.image != 'store_default.png':
                    this.image.delete(save=False)

        except: pass
        super(StoreTable, self).save( *args, **kwargs )



class ProductTable(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255, blank=True, null=True)
    product_review = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    store_link = models.CharField(max_length=500, blank=True, null=True)
    product_specification = models.ForeignKey('ProductSpecificationTable', on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey('StoreTable', models.DO_NOTHING, blank=True, null=True)
    catagory = models.ForeignKey('CatagoryTable', models.DO_NOTHING, blank=True, null=True)
    search_tags = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        default = 'product_pics/product_default.png',
        upload_to = 'product_pics'
        )

    class Meta:
        managed = False
        db_table = 'product_table'
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.product_name

    #Handling Image upload and delete 
    def save(self, *args, **kwargs):
        try:
            this = ProductTable.objects.get(product_id=self.product_id)
            if this.image != self.image:
                if this.image != 'product_default.png':
                    this.image.delete(save=False)

        except: pass
        super(ProductTable, self).save( *args, **kwargs )

    #Enabling Wishlist table to access data through foreign key
    def products(self):
            return Wishlist.objects.filter(wished_product=self)


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
    product = models.ForeignKey('ProductTable', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_specification_table'
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.product_name

    #Enabling ProductTable to access data through foreign key
    def products(self):
            return ProductTable.objects.filter(product_specification=self)

class Wishlist(models.Model):
    table_name = get_user_model()
    user = models.ForeignKey(table_name, on_delete=models.CASCADE)
    wished_product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, blank=True, null=True, default='')

    def __str__(self):
        return self.wished_product.product_name





#Signal for creating slug for catagory table
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=CatagoryTable)
pre_save.connect(slug_generator, sender=BrandTable)
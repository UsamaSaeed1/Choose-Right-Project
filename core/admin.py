from django.contrib import admin
from core.models import (
	CatagoryTable,
	BrandTable,
	StoreTable,
	ProductTable,
	ProductSpecificationTable,
	Wishlist
	)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ('name',)

	filter_horizontal = ()
	list_filter = ()
	fields = ['name']


class BrandAdmin(admin.ModelAdmin):
	list_display = ('name', 'catagory')
	search_fields = ('name',)

	filter_horizontal = ()
	list_filter = ['catagory_id']
	fields = ('name', 'catagory')

class StoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'brand')
	search_fields = ('name',)

	filter_horizontal = ()
	list_filter = ['brand_id']
	fields = ()

class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'catagory', 'product_brand', 'store')
	search_fields = ('product_name',)

	filter_horizontal = ()
	list_filter = ('catagory', 'product_brand', 'store')
	fields = ()
	list_per_page = 25

class SpecificationAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'product_brand', 'release_year', 'touch_screen')
	search_fields = ('product_name',)

	filter_horizontal = ()
	list_filter = ('product_brand', 'release_year', 'touch_screen')
	fields = ()
	list_per_page = 25

admin.site.register(CatagoryTable, CategoryAdmin)
admin.site.register(BrandTable, BrandAdmin)
admin.site.register(StoreTable, StoreAdmin)
admin.site.register(ProductTable, ProductAdmin)
admin.site.register(ProductSpecificationTable, SpecificationAdmin)
from django.contrib import admin
from core.models import (
	CatagoryTable,
	BrandTable,
	StoreTable,
	ProductTable,
	ProductSpecificationTable,
	Wishlist
	)

admin.site.register(CatagoryTable)
admin.site.register(BrandTable)
admin.site.register(StoreTable)
admin.site.register(ProductTable)
admin.site.register(ProductSpecificationTable)
admin.site.register(Wishlist)



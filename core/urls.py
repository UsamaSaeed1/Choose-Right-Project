from django.urls import path
from django.urls import reverse
from . import views as core_views

app_name = 'core'

urlpatterns = [
	path('', core_views.home_view, name='home'),
	path('search/', core_views.search_view, name='search'),
	path('catagory/<slug:slug_text>/', core_views.catagory_view, name='catagory'),
	path('brand/<slug:slug_text>/', core_views.brand_view, name='brand'),
	path('compare/', core_views.compare_view, name='compare'),
	path('add_wishlist/<int:wished_product>/', core_views.add_to_wishlist, name='add_wishlist'),
	path('about/', core_views.about_view, name='about'),
	path('privacy_policy/', core_views.privacy_policy_view, name='privacy_policy'),
	path('terms_of_use/', core_views.terms_of_use_view, name='terms_of_use'),
]

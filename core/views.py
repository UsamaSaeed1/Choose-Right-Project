from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.http import HttpResponse, Http404
from urllib.parse import quote_plus
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import (
	login_required
	)
from django.db.models import (
	Count,
	Subquery,
	Q,
	Avg, Max, Min
	)
from core.models import (
	CatagoryTable,
	BrandTable,
	StoreTable,
	ProductTable,
	ProductSpecificationTable,
	Wishlist
	)
from django.core.paginator import (
	Paginator,
	EmptyPage,
	PageNotAnInteger
	)

def base_view(request):
	return render(request, "chooseright/base.html")

def home_view(request):
	catagory = CatagoryTable.objects.all()
	brand = BrandTable.objects.all()
	product = ProductTable.objects.all()

	# Fetching distinct data from database for product cards
	distinct_product = ProductTable.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count=1)
	records = ProductTable.objects.filter(product_name__in=[item['product_name'] for item in distinct_product])

	#Pagination 
	page = request.GET.get('page',1)
	paginator = Paginator(records, 12)
	try:
		records = paginator.page(page)
	except PageNotAnInteger:
		records = paginator.page(1)
	except EmptyPage:
		records = paginator.page(paginator.num_pages)

	home_dict = {
		'title': 'Choose Right - A Place to Compare Your Choice',
		'catagory': catagory,
		'product_pages': records,
		'brand': brand,
		'product': product,
	}
	return render(request, "chooseright/home.html", home_dict)


def search_view(request):
	catagory = CatagoryTable.objects.all()
	brand = ''

	#Handling user search quries and budget filter
	if request.method == 'GET':
		query = request.GET.get('q')
		price = request.GET.get('price')
		minimum_price = request.GET.get('mini')
		maximum_price = request.GET.get('max')


	if query is not None:
		results = ProductTable.objects.filter(
							Q(product_name__icontains=query) |
							Q(search_tags__icontains=query)
						).distinct()

	active_catagory = results.values('catagory_id')
	for entity in active_catagory:
		active_catagory = entity['catagory_id']
		brand = BrandTable.objects.all().filter(catagory_id=active_catagory)


	#Sorting acording to user preference
	if price == 'asc':
		results = results.order_by('product_price')
	
	elif price == 'desc':
		results = results.order_by('-product_price')

	#Geting product acording to user budget
	if minimum_price and maximum_price:
		if minimum_price !='' and maximum_price !='':
			results = results.order_by('product_price').filter(product_price__gte=minimum_price,product_price__lte=maximum_price).distinct()
			if price == 'asc':
				results = results.order_by('product_price')
		
			elif price == 'desc':
				results = results.order_by('-product_price')


	#Pagination
	page = request.GET.get('page',1)
	paginator = Paginator(results, 12)
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)

	search_dict = {
		'searchtag': request.POST.get('search',''),
		'title': query + ' search results',
		'catagory': catagory,
		'active_catagory': active_catagory,
		'brand': brand,
		'product_pages': results,
		'results': results,
		'tag': 'catagory',
		'query': query,
		'min': minimum_price,
		'max': maximum_price,
		'price': price
	}
	return render(request, "chooseright/searchresults.html", search_dict)


def catagory_view(request, slug_text):
	catagory = CatagoryTable.objects.all()
	products = ProductTable.objects.all()

	#Handling user sorting quries and budget filter
	if request.method == 'GET':
		price = request.GET.get('price')
		minimum_price = request.GET.get('mini')
		maximum_price = request.GET.get('max')

	#determining catagory for submenu
	active_catagory = CatagoryTable.objects.all()
	for entity in active_catagory:
		if entity.slug == slug_text:
			active_catagory = entity.catagory_id

	#Fetching distinct data for the product cards
	distinct_product = ProductTable.objects.filter(catagory_id=active_catagory).values('product_name', 'product_id').distinct()

	#Brands to appear on menu
	brand = BrandTable.objects.filter(catagory_id=active_catagory)

	#Sorting acording to user preference
	if price == 'asc':
		distinct_product = distinct_product.order_by('product_price')
	
	elif price == 'desc':
		distinct_product = distinct_product.order_by('-product_price')

	#Geting product acording to user budget
	if minimum_price and maximum_price:
		if minimum_price !='' and maximum_price !='':
			distinct_product = ProductTable.objects.order_by('product_price').filter(catagory_id=active_catagory,product_price__gte=minimum_price,product_price__lte=maximum_price).values('product_name', 'product_id').distinct()
			if price == 'asc':
				distinct_product = distinct_product.order_by('product_price')
		
			elif price == 'desc':
				distinct_product = distinct_product.order_by('-product_price')

	#Pagination
	product_pages = distinct_product

	page = request.GET.get('page',1)
	paginator = Paginator(product_pages, 12)
	try:
		product_pages = paginator.page(page)
	except PageNotAnInteger:
		product_pages = paginator.page(1)
	except EmptyPage:
		product_pages = paginator.page(paginator.num_pages)
	
	
	result_dict = {
		'title': 'Comapre '+slug_text+' prices',
		'catagory': catagory,
		'brand': brand,
		'tag': 'category',
		'product_pages': product_pages,
		'product': products,
		'slug': slug_text,
		'min': minimum_price,
		'max': maximum_price,
		'price': price
	}
	return render(request, "chooseright/results_page.html", result_dict)


def brand_view(request, slug_text):
	catagory = CatagoryTable.objects.all()
	products = ProductTable.objects.all()

	#Handling user sorting quries and budget filter
	if request.method == 'GET':
		price = request.GET.get('price')
		minimum_price = request.GET.get('mini')
		maximum_price = request.GET.get('max')

	active_catagory = BrandTable.objects.all()
	for entity in active_catagory:
		if entity.slug == slug_text:
			active_catagory = entity.catagory_id

	#Brands to appear on menu
	brand = BrandTable.objects.filter(catagory_id=active_catagory)

	#Products to appear according to brands
	active_brand = brand

	distinct_product = ProductTable.objects.filter(product_brand=slug_text).values('product_name', 'product_id').distinct()

	#Sorting acording to user preference
	if price == 'asc':
		distinct_product = distinct_product.order_by('product_price')
	
	elif price == 'desc':
		distinct_product = distinct_product.order_by('-product_price')

	#Geting product acording to user budget
	if minimum_price and maximum_price:
		if minimum_price !='' and maximum_price !='':
			distinct_product = ProductTable.objects.order_by('product_price').filter(product_brand=slug_text,product_price__gte=minimum_price,product_price__lte=maximum_price).values('product_name', 'product_id').distinct()
			if price == 'asc':
				distinct_product = distinct_product.order_by('product_price')
		
			elif price == 'desc':
				distinct_product = distinct_product.order_by('-product_price')

	#Pagination
	product_pages = distinct_product
	page = request.GET.get('page',1)
	paginator = Paginator(product_pages, 12)
	try:
		product_pages = paginator.page(page)
	except PageNotAnInteger:
		product_pages = paginator.page(1)
	except EmptyPage:
		product_pages = paginator.page(paginator.num_pages)
	
	result_dict = {
		'title': 'Comapre '+slug_text+' products',
		'catagory': catagory,
		'brand': brand,
		'tag': 'brand',
		'product_pages': product_pages,
		'product': products,
		'slug': slug_text,
		'min': minimum_price,
		'max': maximum_price,
		'price': price,
	}
	return render(request, "chooseright/results_page.html", result_dict)

def compare_view(request):
	catagory = CatagoryTable.objects.all()
	store = StoreTable.objects.all()
	current_user = request.user

	#Handling user compare request
	if request.GET.get('p_name'):
		p_name = request.GET.get('p_name')
		if p_name =='':
			raise Http404

	else:
		raise Http404

	share_string = quote_plus(p_name)
	query = ProductTable.objects.all().order_by('product_price').filter(product_name__iexact=p_name)

	if not query:
		raise Http404

	#Handling comparison for the product
	com_list = ProductTable.objects.filter(product_name__iexact=p_name).aggregate(min_price=Min('product_price'), max_price=Max('product_price'))

	#Getting users wish list information
	current_list = Wishlist.objects.all().filter(user_id__exact=current_user.id).filter(slug__exact=p_name)

	active_catagory = query.values('catagory_id')
	for entity in active_catagory:
		active_catagory = entity['catagory_id']
		brand = BrandTable.objects.all().filter(catagory_id=active_catagory)
	
	compare_dict = {
		'title': 'Choose Right - A Place to Compare Your Choice',
		'catagory': catagory,
		'brand': brand,
		'store': store,
		'share_string': share_string,
		'query': query,
		'com_list': com_list,
		'current_list': current_list,
	}
	return render(request, "chooseright/compare.html", compare_dict)

def add_to_wishlist(request, wished_product):
	if request.user.is_authenticated:
		return add_to_wishlist_verified(request, wished_product)

	else:
		messages.warning(request, f'You must log-in first in order to add product to wishlist')
		return redirect('users:login')

@login_required()
def add_to_wishlist_verified(request, wished_product):
	current_user = request.user
	wishlist_product = wished_product
	product = request.GET.get('p_name')
	wishlist = request.GET.get('wishlist')

	if wished_product == '':
		raise Http404

	else:
		current_list = Wishlist.objects.all().filter(user_id__exact=current_user.id).filter(wished_product_id__exact=wishlist_product)
	
	if wishlist:
		remove =  Wishlist.objects.all().filter(user_id__exact=current_user.id).filter(wished_product_id__exact=wishlist_product)
		remove.delete()
		messages.success(request, f'Product successfully removed from wishlist.')

	else:
		if not current_list:
			wishlist_products = Wishlist(user_id=current_user.id, wished_product_id=wishlist_product, slug=product)
			wishlist_products.save()
			messages.success(request, f'Product successfully added to wishlist.')

		else:
			messages.warning(request, f'Product already exists in wishlist')
	
	return compare_view(request)


def about_view(request):
	return render(request, 'chooseright/about.html', {'title': 'About Us - Choose Right'})


def privacy_policy_view(request):
	return render(request, 'chooseright/privacy-policy.html',{'title': 'Privacy Policy - Choose Right'})

def terms_of_use_view(request):
	return render(request, 'chooseright/terms_of_use.html',{'title': 'Terms of Use - Choose Right'})

	

def error_404(request, exception, template_name='404.html'):
        data = {
        'status': 404
        }
        return render(request, template_name, data)

def error_500(request, template_name='500.html'):
        data = {
        'status': 500
        }
        return render(request, template_name, data)
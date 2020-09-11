from django.shortcuts import (render,
	redirect,
	get_object_or_404,
	HttpResponseRedirect
	)

from .forms import (
	UserRegisterForm,
	UserUpdateForm,
	ProfileUpdateForm,
	LoginForm
	)

from django.contrib import messages
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.forms import (
	PasswordChangeForm,
	PasswordResetForm,
	SetPasswordForm,
	)
from django.contrib.auth import (
	update_session_auth_hash,
	logout
	)
from django.contrib.auth.decorators import (
	login_required,
	user_passes_test
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
from django.contrib.auth import views as auth_views
from tellme.models import Feedback



# Decorators to restrict user activity
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = settings.LOGIN_REDIRECT_URL

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous(),
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


# Views for User Module

#Verifying user is not logged-in before creating new account
def register_view(request):
	if request.user.is_authenticated:
		messages.warning(request, f'You must logout first in order to create a new account')
		return dash_board_view_access(request)
	else:
		return register_view_verified(request)


#View to handle user requests for registration
def register_view_verified(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created ! You can now log-in')
			return redirect('users:login')

	else:
		form = UserRegisterForm()

	register_view_dict = {
		'form': form,
		'title':'Create Your Account - Choose Right'
		}

	return render(request, 'users/register.html', register_view_dict)



# Class based view for log-out
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login - Choose Right'
        return context

# Handling log-out request
def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next'))



# Class based views for password reset proccess
class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = '/account/password_reset/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset Password - Choose Right'
        return context

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset Password - Choose Right'
        return context

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	form_class = SetPasswordForm
	template_name = 'users/password_reset_confirm.html'
	success_url = '/account/password_reset_complete/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reset Password - Choose Right'
		return context

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset Password Complete - Choose Right'
        return context


# Views for User Account Options


#Dashboard view/ Users main profile view
def dash_board_view(request):
    if request.user.is_anonymous:
        messages.warning(request, f'You must log-in first to access your account page.')

    return dash_board_view_access(request)


@login_required()
def dash_board_view_access(request):
	if request.user.first_name:
		title = request.user.first_name
	else:
		title = request.user.username

	current_user = request.user
	catagory = CatagoryTable.objects.all()

	wishlist = Wishlist.objects.all().filter(user_id__exact=current_user.id).count()
	feedback = Feedback.objects.all().filter(user_id__exact=current_user.id).count()

	dash_board_view_dict = {
		'title': title+"'s" + ' Profile - Choose Right',
		'wishlist': wishlist,
		'feedback': feedback,
		'catagory': catagory
		}
	return render(request, 'users/dash-board.html',dash_board_view_dict)


#Users wishlist view
def wish_list_view(request):
    if request.user.is_anonymous:
        messages.warning(request, f'You must log-in first to access your wishlist page.')
    return wish_list_view_access(request)


@login_required()  
def wish_list_view_access(request):
	current_user = request.user
	wishlist = Wishlist.objects.all().filter(user_id__exact=current_user.id)
	catagory = CatagoryTable.objects.all()

	#Pagination 
	page = request.GET.get('page',1)
	paginator = Paginator(wishlist, 12)
	try:
		wishlist = paginator.page(page)
	except PageNotAnInteger:
		wishlist = paginator.page(1)
	except EmptyPage:
		wishlist = paginator.page(paginator.num_pages)

	wishlist_dict = {
		'title': 'Wishlist',
		'wishlist': wishlist,
		'product_pages': wishlist,
		'catagory': catagory
	}
	return render(request, 'users/wishlist.html', wishlist_dict)

#Users reviews/feedback view
def feedback_view(request):
    if request.user.is_anonymous:
        messages.warning(request, f'You must log-in first to access your review page.')
    return feedback_view_access(request)


@login_required()  
def feedback_view_access(request):
	current_user = request.user
	feedback = Feedback.objects.all().filter(user_id__exact=current_user.id)
	catagory = CatagoryTable.objects.all()

	feedback_dict = {
		'title': 'Feedback',
		'feedback': feedback,
		'catagory': catagory
	}
	return render(request, 'users/reviews.html',feedback_dict)



def profile_view(request):
    if request.user.is_anonymous:
        messages.warning(request, f'You must log-in first to view your profile.')
    return profile_view_access(request)


@login_required()  
def profile_view_access(request):
	catagory = CatagoryTable.objects.all()
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,
								instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
									request.FILES,
									instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated successfully.')
			return redirect('users:profile')


	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	profile_dict = {
		'title': 'Update Profile Information',
		'u_form': u_form,
		'p_form': p_form,
		'catagory': catagory
	}

	return render(request, 'users/profile.html', profile_dict)


def change_password_view(request):
    if request.user.is_anonymous:
        messages.warning(request, f'You must log-in first.')
    return change_password_view_access(request)


@login_required() 
def change_password_view_access(request):
	catagory = CatagoryTable.objects.all()
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, f'Your password has been updated successfully.')
			return redirect('users:dash_board')


	else:
		form = PasswordChangeForm(user = request.user)

	change_password_view_dic = {
		'title': 'Change Password',
		'form': form,
		'catagory': catagory
	}
	return render(request, 'users/change_password.html', change_password_view_dic)





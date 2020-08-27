from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile


YEARS= [x for x in range(1980,2021)]
Gender_Option = (
    ('M','Male'),
    ('F','Female'),
    )


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(
		label='Username',
		)

	first_name = forms.CharField(
		label='First Name',
		required=False,
		)

	last_name = forms.CharField(
		label='Last Name',
		max_length=100
		)

	email = forms.EmailField()

	password1 = forms.CharField(label='Password')

	password2 = forms.CharField(label='Confirm Password')

	class Meta:
		model = get_user_model()
		fields = [
		'email',
		'username',
		'first_name',
		'last_name',
		'password1',
		'password2',
		]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

    

class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField(
		label='First Name',
		required=False,
		max_length=100
		)

	last_name = forms.CharField(
		label='Last Name',
		required=False,
		max_length=100)

	email = forms.EmailField()

	class Meta:
		model = get_user_model()
		fields = [	
		'first_name',
		'last_name',
		'email',
		]


class ProfileUpdateForm(forms.ModelForm):
	birth_date= forms.DateField(
		label='Date of Birth',
		required=False,
		widget=forms.SelectDateWidget(years=YEARS,))

	city = forms.CharField(
		label='City',
		required=False,
		)

	gender = forms.ChoiceField(
		choices = Gender_Option,
		required=False,
		widget=forms.RadioSelect())

	class Meta:
		model = Profile
		fields =[
		'birth_date',
		'city',
		'gender',
		'image',
		]
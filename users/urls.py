from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import reverse
from . import views as user_view

app_name = 'users'

urlpatterns = [

    path('register/', user_view.register_view, name="register"),

    path('login/',
    	user_view.LoginView.as_view(redirect_authenticated_user = True),
    	name='login'),

    path('logout/', user_view.logout_view, name="logout"),

    path('password_reset/',
    	user_view.PasswordResetView.as_view(),
    	name='password_reset'),

    path('password_reset/done/',
    	user_view.PasswordResetDoneView.as_view(),
    	name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>',
    	user_view.PasswordResetConfirmView.as_view(),
    	name='password_reset_confirm'),

    path('password_reset_complete/',
    	user_view.PasswordResetCompleteView.as_view(),
    	name='password_reset_complete'),

    path('dash_board/', user_view.dash_board_view, name="dash_board"),
    path('wish_list/', user_view.wish_list_view, name="wish_list"),
    path('feedback/', user_view.feedback_view, name="feedback"),
    path('change_password/', user_view.change_password_view, name="change_password"),
    path('profile_update/', user_view.profile_view, name="profile"),

]

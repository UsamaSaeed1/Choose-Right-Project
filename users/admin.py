from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.functions import ExtractYear
from django.utils.translation import gettext_lazy as _
from .models import Profile, User

class UsersAdmin(UserAdmin):
	list_display = ('username', 'email', 'date_joined', 'last_login', 'is_staff')
	search_fields = ('username', 'email',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ('is_staff','is_active')
	feildsets = ()

class SearchByYear(admin.SimpleListFilter):
    title = _('Birth Year')
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        year_list = Profile.objects.annotate(
            y=ExtractYear('birth_date')
        ).order_by('y').values_list('y', flat=True).distinct()
        return [
            (str(y), _(str(y))) for y in year_list
        ]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(date__year=self.value())
        return queryset

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'birth_date', 'gender')
	search_fields = ('user__username',)
	date_hierarchy = 'birth_date'

	
	filter_horizontal = ()
	list_filter = (SearchByYear,'gender')
	fields = ()
	ordering = ['user']

admin.site.register(User, UsersAdmin)
admin.site.register(Profile, ProfileAdmin)

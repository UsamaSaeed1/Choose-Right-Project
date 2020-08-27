from django.db.models.signals import post_save

from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

#Every time a new user data is saved this function will create a profile for that user
@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


#Every time a new user profile is created, this function will save that profile for the user
@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import datetime
from PIL import Image


Gender_Option = (
    ('M','Male'),
    ('F','Female'),
    )

#Custom model to make sure that that email feild is unique for each user
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username



class Profile(models.Model):
    table_name = get_user_model()
    user = models.OneToOneField(table_name, on_delete=models.CASCADE)
    image = models.ImageField(
        default = 'profile_pics/default.jpg',
        upload_to = 'profile_pics'
        )
    birth_date = models.DateField(
        blank = True,
        verbose_name = 'Date of Birth',
        null=True
        )
    gender = models.CharField(
        blank = True,
        choices = Gender_Option,
        max_length = 1, default = '',
        verbose_name = 'Gender',
        null=True
        )
    city = models.CharField(
        blank = True,
        null = True,
        max_length = 50,
        default = '',
        verbose_name = 'City'
        )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image:
                if this.image != 'profile_pics/default.jpg':
                    this.image.delete(save=False)

        except: pass
        super(Profile, self).save( *args, **kwargs )

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


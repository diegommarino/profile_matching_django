from django.db import models


def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.user_id, filename)


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_position = models.CharField(max_length=64)
    avatar = models.ImageField(blank=True, null=True, upload_to=upload_to)
    about = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)

    class Meta:
        ordering = ('first_name',)

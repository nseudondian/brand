from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profiles
from django.contrib.auth.models import User



@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = profiles.objects.create(user=user)
        profile.save()
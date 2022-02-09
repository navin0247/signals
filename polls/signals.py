# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print("calling create_profile")
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    print(sender)
    print(instance)
    print("calling save_profile")
    instance.profile.save()


post_save.connect(save_profile, sender=User)

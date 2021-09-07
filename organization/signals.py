from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    print("Inactivating user!")
    if instance._state.adding:
        # instance.is_active = False
        print("user inactivated!")

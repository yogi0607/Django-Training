from django.contrib.auth.models import User
from .models import PMProfile
from django.db.models.signals import post_save, post_delete


def createManager(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = PMProfile.objects.create(
            user = user,
        )

def deleteManager(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createManager, sender = User)

post_delete.connect(deleteManager, sender = PMProfile)

# def managercreated(sender, instance, created, **kwargs):
#     print('profile saved')
#     print('instance: ', instance)
#     print('CREATED: ', created)

# post_save.connect(managercreated, sender=PMProfile)
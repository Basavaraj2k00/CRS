from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from realtors.models import Owner
from listings.models import Listing

def create_listing(sender, instance, created, **kwargs):
    if created:
        Listing.objects.create(
            owner = instance.owner,
            
        )
        print('Listing created!')
    else:
        print("something went wrong")



post_save.connect(create_listing, sender=User)
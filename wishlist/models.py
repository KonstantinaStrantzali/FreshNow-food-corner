from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):

    """
    Model to show all product items within the users wishlist
    """
    profile_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'wishlist ({self.profile_user})'

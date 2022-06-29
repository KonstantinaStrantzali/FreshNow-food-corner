from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Reviews(models.Model):
    
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    profile_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    review = models.TextField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f'User: {self.profile_user} | Product: {self.product} | \
                    Rating: {self.rating}'

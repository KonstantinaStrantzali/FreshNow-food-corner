from django.contrib import admin
from .models import Reviews

# Register your models here.



class ReviewAdmin(admin.ModelAdmin):

    model = Reviews
    list_display = (
        'profile_user',
        'product',
        'rating',
        'review',
        'created_date',
    )

    ordering = ('-created_date', '-rating', )
    
admin.site.register(Reviews)
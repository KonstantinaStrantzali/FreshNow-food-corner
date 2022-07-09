from django import forms
from reviews.models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ('profile_user', 'product', 'created_date')

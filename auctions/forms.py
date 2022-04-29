from django.db import models
from django.forms import ModelForm

from auctions.models import AuctionListing
# class imageform(models.Model):
#     # class Meta:
#     model = AuctionListing
#     fields = ['imageUrl']
    # img = models.ImageField(upload_to='images/')

class AuctionListingForm(ModelForm):
    # class Meta:
    class Meta:
        model = AuctionListing
        # fields = '__all__'
        fields = ['category','name','description','imageUrl']
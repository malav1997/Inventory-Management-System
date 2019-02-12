from django import forms
from django.contrib.auth.models import User
from basic.models import Item, Stock

class SellForm(forms.ModelForm):

	class Meta:
		model = Stock
		fields= ('master', 'item', 'quantity', 'stored_date', )


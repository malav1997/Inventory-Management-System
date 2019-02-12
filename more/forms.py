from django import forms
from basic.models import  Item

class ItemForm(forms.ModelForm):

	class Meta:
		model= Item
		fields= ('name', 'max_storage_temperature', 'min_storage_temperature', 'max_storage_time', 'price', )
			
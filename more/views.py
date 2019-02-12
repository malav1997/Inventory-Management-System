from django.shortcuts import render
from basic.models import Item
from .forms import ItemForm


# Create your views here.
def more(request):
	form = ItemForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return render(request, 'more/more.html', {'form': form})
	else:
		return render(request, 'more/more.html', {'form': form})

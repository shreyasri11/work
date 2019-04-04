from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import MenuUpdateForm, TimingUpdateForm
from .models import Item, Timing
# Create your views here.


def MenuListView(request):
	context = {
		'timing':Timing.objects.all().first(),
		'menu':Item.objects.all()
	}
	return render(request, 'menu/menu_list.html', context)


def MenuUpdateView(request, id=None):
	instance = get_object_or_404(Item, id=id)
	form = MenuUpdateForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("menu:menu"))
	context = {
		'form':form,
		'title':'MenuUpdate',
	}
	return render(request, 'menu/form.html', context)

def TimingUpdateView(request, id=None):
	instance = get_object_or_404(Timing, id=id)
	form = TimingUpdateForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("menu:menu"))
	context = {
		'form':form,
		'title':'TimingUpdate',
	}
	return render(request, 'menu/form.html', context)

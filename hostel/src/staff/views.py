from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Staff, Post
from .forms import StaffForm, PostForm

def StaffListView(request):
	 staff = Staff.objects.all()
	 return render(request, 'staff/list.html', {'staff':staff, 'title':'Staff'})

def StaffDetailView(request, id=None):
	instance = get_object_or_404(Staff, id=id)
	return render(request, 'staff/detail.html', {'instance':instance,'title':'Staff'})

def StaffAddView(request):
	form = StaffForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("staff:list"))
	context = {
		'form':form,
		'title':'Staff Add',
		'btn_title':'Submit',
	}
	return render(request, 'staff/form.html', context)

def StaffUpdateView(request, id=None):
	instance = get_object_or_404(Staff, id=id)
	form = StaffForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("staff:detail" ,kwargs={'id':instance.id}))
	context = {
		'form':form,
		'title':'StaffUpdate',
		'btn_title':'Update',
	}
	return render(request, 'staff/form.html', context)

def StaffDeleteView(request, id=None):
	instance = get_object_or_404(Staff, id=id)
	if request.method=="POST":
		instance.delete()
		return HttpResponseRedirect(reverse("staff:list"))

	context = {
		'instance':instance,
		'title':'Staff'
	}
	return render(request, 'staff/delete.html' ,context)



def PostListView(request):
	post = Post.objects.all()
	return render(request, 'staff/postlist.html', {'post':post, 'title':'Post'})

def PostAddView(request):
	form = PostForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("staff:post_list"))
	context = {
		'form':form,
		'title':'Post Add',
		'btn_title':'Submit',
	}
	return render(request, 'staff/form.html', context)

def PostUpdateView(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("staff:post_list"))
	context = {
		'form':form,
		'title':'PostUpdate',
		'btn_title':'Update',
	}
	return render(request, 'staff/form.html', context)

def PostDeleteView(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if request.method=="POST":
		instance.delete()
		return HttpResponseRedirect(reverse("staff:post_list"))

	context = {
		'instance':instance,
		'title':'Post'
	}
	return render(request, 'staff/post_delete.html' ,context)



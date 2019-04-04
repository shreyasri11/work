from django.conf.urls import url
from .views import (
	StaffListView, 
	StaffUpdateView, 
	StaffDetailView, 
	StaffAddView, 
	StaffDeleteView,
	PostListView,
	PostAddView,
	PostUpdateView,
	PostDeleteView,
	)

urlpatterns = [
    url(r'^$',StaffListView , name="list"),
    url(r'^add/$', StaffAddView, name="add"),
    url(r'^(?P<id>\d+)/$', StaffDetailView, name="detail"),
    url(r'^(?P<id>\d+)/update/$', StaffUpdateView, name='update'),
    url(r'^(?P<id>\d+)/delete/$', StaffDeleteView, name='delete'),
    url(r'^post/$',PostListView , name="post_list"),
    url(r'^post/add/$',PostAddView , name="post_add"),
    url(r'^post/(?P<id>\d+)/update/$', PostUpdateView, name='post_update'),
    url(r'^post/(?P<id>\d+)/delete/$', PostDeleteView, name='post_delete'),
]


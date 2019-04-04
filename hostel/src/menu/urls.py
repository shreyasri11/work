from django.conf.urls import url
from .views import MenuListView, MenuUpdateView, TimingUpdateView

urlpatterns = [
    
    url(r'^$', MenuListView, name="menu"),
    url(r'^(?P<id>\d+)/$', MenuUpdateView, name='update'),
    url(r'^timing/(?P<id>\d+)/$', TimingUpdateView, name='timing_update'),
    
]
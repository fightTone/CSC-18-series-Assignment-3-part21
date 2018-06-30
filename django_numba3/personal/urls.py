from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from personal.models import Stories

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^write/$', views.write, name='write'),
	url(r'^writing/$', views.writing, name='writing'),
	url(r'^updating/(?P<id>\d+)$', views.updating, name='updating'),
	url(r'^update/(?P<pk>\d+)$', DetailView.as_view(model = Stories,
		template_name = 'personal/update.html')),
	# url(r'^stories/$', views.stories, name='stories'),
	url(r'^stories/$', ListView.as_view(queryset = Stories.objects.all().order_by("-date")[:25],
		template_name="personal/stories.html")),
	url(r'^stories/(?P<pk>\d+)$', DetailView.as_view(model = Stories,
		template_name = 'personal/post.html')),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
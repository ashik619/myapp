from django.conf.urls import url
from . import views
from blog.views import RESTpostapi
urlpatterns = [
    url(r'^home$', views.post_list, name='post_list'),
	url(r"^rest/(?P<pk>[0-9]+)/$",RESTpostapi.as_view(),name="rsetapi"),
]
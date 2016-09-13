from django.conf.urls import url
from . import views
from carapp.views import RESTcarapi
urlpatterns = [
	#url(r"^/rest/(?P<pk>[0-9]+)/$",RESTcarapi.as_view(),name="rsetapi"),
]
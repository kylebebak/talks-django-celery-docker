from django.contrib import admin
from django.conf.urls import include, url

from api import views


urlpatterns = (
    url(r'^my_endpoint/$', views.MyEndpoint.as_view(), name='my-endpoint'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

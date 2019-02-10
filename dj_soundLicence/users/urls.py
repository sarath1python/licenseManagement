from django.conf.urls import url

from .views import UserCreate


urlpatterns = [
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # url(r'^users/list/$', UserList.as_view()),
    url(r'^users/create/$', UserCreate.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view())
]
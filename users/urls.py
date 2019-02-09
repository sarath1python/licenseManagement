from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from .views import UserCreate,login_view, home_view


urlpatterns = [
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # url(r'^users/list/$', UserList.as_view()),
    url(r'^users/create/$', UserCreate.as_view()),
    url(r'^login/$',login_view),
    url(r'^home/',home_view, name='home')
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view())
]
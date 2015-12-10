from django.conf.urls import url

from .views import (
    addto_all,
    addto_user,
    invite,
    topoff_all,
    invite_stat,
    topoff_user
)


urlpatterns = [
    url(r"^invite/$", invite, name="pinax-invitations-invite"),
    url(r"^invite-stat/(?P<pk>\d+)/$", invite_stat, name="pinax-invitations-invite_stat"),
    url(r"^topoff/$", topoff_all, name="pinax-invitations-topoff_all"),
    url(r"^topoff/(?P<pk>\d+)/$", topoff_user, name="pinax-invitations-topoff_user"),
    url(r"^addto/$", addto_all, name="pinax-invitations-addto_all"),
    url(r"^addto/(?P<pk>\d+)/$", addto_user, name="pinax-invitations-addto_user"),
]

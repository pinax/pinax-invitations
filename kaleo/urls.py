from django.conf.urls import url, patterns

from kaleo.views import (
    addto_all,
    addto_user,
    invite,
    topoff_all,
    invite_stat,
    topoff_user
)


urlpatterns = patterns(
    "",
    url(r"^invite/$", invite, name="kaleo_invite"),
    url(r"^invite-stat/(?P<pk>\d+)/$", invite_stat, name="kaleo_invite_stat"),
    url(r"^topoff/$", topoff_all, name="kaleo_topoff_all"),
    url(r"^topoff/(?P<pk>\d+)/$", topoff_user, name="kaleo_topoff_user"),
    url(r"^addto/$", addto_all, name="kaleo_addto_all"),
    url(r"^addto/(?P<pk>\d+)/$", addto_user, name="kaleo_addto_user"),
)

from django.conf.urls import url

from .views import (
    AddToAllView,
    AddToUserView,
    InviteStatView,
    InviteView,
    TopOffAllView,
    TopOffUserView,
)

app_name = "pinax_invitations"

urlpatterns = [
    url(r"^invite/$", InviteView.as_view(), name="invite"),
    url(r"^invite-stat/(?P<pk>\d+)/$", InviteStatView.as_view(), name="invite_stat"),
    url(r"^topoff/$", TopOffAllView.as_view(), name="topoff_all"),
    url(r"^topoff/(?P<pk>\d+)/$", TopOffUserView.as_view(), name="topoff_user"),
    url(r"^addto/$", AddToAllView.as_view(), name="addto_all"),
    url(r"^addto/(?P<pk>\d+)/$", AddToUserView.as_view(), name="addto_user"),
]

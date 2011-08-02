from django.conf.urls.defaults import url, patterns

from invitations.views import invite


urlpatterns = patterns("",
    url(r"^invite/$", invite, name="invitations_invite"),
)

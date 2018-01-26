from django.conf.urls import include, url

urlpatterns = [
    url(r"^account", include("account.urls")),
    url(r"^", include("pinax.invitations.urls", namespace="pinax_invitations")),
]

from django.conf.urls import url, include


urlpatterns = [
    url(r"^", include("pinax.invitations.urls", namespace="pinax_invitations")),
]

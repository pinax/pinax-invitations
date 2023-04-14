from django.urls import include, re_path

urlpatterns = [
    re_path(r"^account", include("account.urls")),
    re_path(r"^", include("pinax.invitations.urls", namespace="pinax_invitations")),
]

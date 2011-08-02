import django.dispatch


invite_sent = django.dispatch.Signal(providing_args=["invitation",])
invite_accepted = django.dispatch.Signal(providing_args=["invitation"])

import django.dispatch

invite_sent = django.dispatch.Signal()
invite_accepted = django.dispatch.Signal()
joined_independently = django.dispatch.Signal()

import django


__all__ = ["get_user_model"]


# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model
else:
    from django.contrib.auth.models import User
    get_user_model = lambda: User

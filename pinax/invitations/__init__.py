import pkg_resources


__version__ = pkg_resources.get_distribution("pinax-invitations").version
default_app_config = "pinax.invitations.apps.AppConfig"

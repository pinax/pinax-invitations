from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pinax-invitations")
except PackageNotFoundError:
    __version__ = "unknown"

default_app_config = "pinax.invitations.apps.AppConfig"

from distutils.core import setup


setup(
    name = "invitations",
    version = "0.1.dev2",
    description = "an invitations app",
    url = "https://github.com/eldarion/django-invitations",
    author = "Eldarion",
    author_email = "opensource@eldarion.com",
    packages = [
        "invitations",
        "invitations.templatetags"
    ],
    package_data = {
            "invitations": [
                "templates/invitations/*.html",
            ]
        },
    zip_safe = False
)

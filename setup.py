from distutils.core import setup


setup(
    name = "kaleo",
    version = "0.1.dev2",
    description = "an user to user join invitations app",
    url = "https://github.com/eldarion/kaleo",
    author = "Eldarion",
    author_email = "paltman@eldarion.com",
    packages = [
        "kaleo",
        "kaleo.templatetags"
    ],
    package_data = {
            "kaleo": [
                "templates/kaleo/*.html",
            ]
        },
    zip_safe = False
)

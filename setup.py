import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a user to user join invitations app",
    name="pinax-invitations",
    long_description=read("README.rst"),
    version="4.0.2",
    url="http://github.com/pinax/pinax-invitations/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "invitations": []
    },
    test_suite="runtests.runtests",
    install_requires=[
        "django-appconf>=1.0.1",
        "django-user-accounts>=1.3"
    ],
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)

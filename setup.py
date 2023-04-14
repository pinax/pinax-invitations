from setuptools import find_packages, setup

VERSION = "7.1.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-invitations.svg
    :target: https://pypi.python.org/pypi/pinax-invitations/

=================
Pinax Invitations
=================

.. image:: https://img.shields.io/pypi/v/pinax-invitations.svg
    :target: https://pypi.python.org/pypi/pinax-invitations/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-invitations.svg
    :target: https://circleci.com/gh/pinax/pinax-invitations
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-invitations.svg
    :target: https://codecov.io/gh/pinax/pinax-invitations
.. image:: https://img.shields.io/github/contributors/pinax/pinax-invitations.svg
    :target: https://github.com/pinax/pinax-invitations/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-invitations.svg
    :target: https://github.com/pinax/pinax-invitations/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-invitations.svg
    :target: https://github.com/pinax/pinax-invitations/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

``pinax-invitations`` is a user to user join invitations app.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 3.7 | 3.8 | 3.9 | 3.10 |
+=================+=====+=====+=====+=====+
|  3.2            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+=====+
|  4.0            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+=====+
|  4.1            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a user to user join invitations app",
    name="pinax-invitations",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-invitations/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "invitations": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=3.2",
        "django-appconf>=1.0.5",
        "django-user-accounts>=3.2.0",
    ],
    test_suite="runtests.runtests",
    tests_require=[
        "django-test-plus",
        "pinax-templates>=3.0.0",
    ],
    zip_safe=False,
)

from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/blank.svg
    :target: https://pypi.python.org/pypi/pinax-invitations/

=================
Pinax Invitations
=================

.. image:: https://img.shields.io/pypi/v/pinax-invitations.svg
    :target: https://pypi.python.org/pypi/pinax-invitations/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-invitations/

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

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/


``pinax-invitations`` is a user to user join invitations app.


Supported Django and Python Versions
------------------------------------

* Django 1.8, 1.10, 1.11, and 2.0
* Python 2.7, 3.4, 3.5, and 3.6
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a user to user join invitations app",
    name="pinax-invitations",
    long_description=LONG_DESCRIPTION,
    version="5.1.0",
    url="http://github.com/pinax/pinax-invitations/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "invitations": []
    },
    install_requires=[
        "django-appconf>=1.0.1",
        "django-user-accounts>=1.3",
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)

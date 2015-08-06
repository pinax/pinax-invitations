pinax-starter-app
=================
.. image:: http://slack.pinaxproject.com/badge.svg
   :target: http://slack.pinaxproject.com/

Quickly setup the scaffolding for your django app.

What you get:

* test infrastructure
* Travis configuration with coveralls
* documentation instrastructure
* MIT LICENSE
* setup.py


Getting Started
================

Execute::

    pip install Django
    django-admin.py startapp --template=https://github.com/pinax/pinax-starter-app/zipball/master --extension=py,rst,in,sh,rc,yml,ini,coveragerc <project_name>


After you are running you have a fresh app, first update this readme by removing
everything above and including this line and unindenting everything below this line. Also
remember to edit the ``<user_or_org_name>`` in the travis and coveralls badge/links::

    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps. To learn more about Pinax,
    see http://pinaxproject.com/

    pinax-invitations
    ========================

    .. image:: https://img.shields.io/travis/<user_or_org_name>/pinax-invitations.svg
        :target: https://travis-ci.org/<user_or_org_name>/pinax-invitations

    .. image:: https://img.shields.io/coveralls/<user_or_org_name>/pinax-invitations.svg
        :target: https://coveralls.io/r/<user_or_org_name>/pinax-invitations

    .. image:: https://img.shields.io/pypi/dm/pinax-invitations.svg
        :target:  https://pypi.python.org/pypi/pinax-invitations/

    .. image:: https://img.shields.io/pypi/v/pinax-invitations.svg
        :target:  https://pypi.python.org/pypi/pinax-invitations/

    .. image:: https://img.shields.io/badge/license-<license>-blue.svg
        :target:  https://pypi.python.org/pypi/pinax-invitations/


    Documentation can be found at http://docs.pinaxproject.com/pinax-invitations/


    Running the Tests
    ------------------------------------

    ::

        $ pip install detox
        $ detox

.. _installation:

Installation
============

* To install Django Invitations::

    pip install django-invitations --extra-index-url=http://dist.pinaxproject.com/dev/

* Add ``'invitations'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # other apps
        "invitations",
    )

* See the list of :ref:`settings` to modify Django Invitations's
  default behavior and make adjustments for your website.

.. _dependencies:

Dependencies
------------

django-email-confirmation_
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used for linking people to invitations when they confirm email addresses.


pinax.apps.signup_codes_
^^^^^^^^^^^^^^^^^^^^^^^^

Used to manage the sending and processing of signup codes via email.


.. _django-email-confirmation: http://github.com/pinax/django-email-confirmation
.. _pinax.apps.signup_codes: http://github.com/pinax/pinax

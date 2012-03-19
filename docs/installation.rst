.. _installation:

Installation
============

* To install kaleo::

    pip install kaleo

* Add ``kaleo`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # other apps
        "kaleo",
    )

* See the list of :ref:`settings` to modify kaleo's
  default behavior and make adjustments for your website.

* Lastly you will want to add `kaleo.urls` to your urls definition::

    ...
    url(r"^invites/", include("kaleo.urls")),
    ...


.. _dependencies:

Dependencies
------------

pinax-theme-bootstrap_
^^^^^^^^^^^^^^^^^^^^^^

This is semi-optional as the only reason it is required is the included
`_invite_form.html` renders the form through the `as_bootstrap` filter. If
you override this template in your project, you obviously remove this
requirement at least in context of this app.


django-user-accounts_
^^^^^^^^^^^^^^^^^^^^^

Used for linking people to invitations when they confirm email addresses and
sending and processing of signup codes via email.

.. _django-uni-form: https://github.com/pydanny/django-uni-form
.. _django-user-accounts: http://github.com/pinax/django-user-accounts

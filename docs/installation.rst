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

eldarion-ajax_
^^^^^^^^^^^^^^^

This is used to enable the markup based ajax. You can certain wire up your
own AJAX handling if you prefer to use something else. However, including
this script will just have things work out of the box.


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


.. _bootstrap-ajax: http://github.com/eldarion/bootstrap-ajax
.. _pinax-theme-bootstrap: http://github.com/pinax/pinax-theme-bootstrap
.. _django-user-accounts: http://github.com/pinax/django-user-accounts

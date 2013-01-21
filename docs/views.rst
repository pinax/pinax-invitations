.. _views:

Views
=====

There are four different views designed to handle POSTs via AJAX with
a single variable, ``amount``. These are designed to be able to help
administrators manage invites from a front-end dashboard. The responses
sent from these views conform to what ``bootstrap-ajax`` expects and
works with.

They all require the user has the permission ``kaleo.manage_invites``
which is up to the site developer to determine how to and who to grant
this to or evaluate in a custom auth backend. The largest use case
should already be covered in that any user with staff or superuser
privileges should supercede the need for this explicit permission.


topoff_all
----------

:url: kaleo_topoff_all

Tops off all users with at least ``amount`` invites.

Returns::

    {
        "inner-fragments": {
            ".invite-total": amount
        }
    }


topoff_user
-----------

:url: kaleo_topoff_user user.pk

Tops off ``{{ user.pk }}`` with at least ``amount`` invites.

Returns::

    {
        "html": amount
    }


addto_all
---------

:url: kaleo_addto_all

Adds ``number`` invites to all users

Returns::

    {
        "inner-fragments": {
            ".amount-added": amount
        }
    }


addto_user
----------

:url: kaleo_addto_user user.pk

Adds ``number`` invites to ``{{ user.pk }}``

Returns::

    {
        "inner-fragments": {
            ".html": amount
        }
    }


invite_stat
-----------

:url: kaleo_invite_stat user.pk

Returns a rendered ``kaleo/_invite_stat.html`` fragment to be supplied by the
site developer to render an ``InvitationStat`` object for the ``user.pk`` provided
to the template with the context variable ``stat``.

The intended purpose for this is to used as a ``data-refresh-url`` for ``bootstrap-ajax``.

Returns::

    {
        "html": <rendered kaleo/_invite_stat.html>  # provided by site developer
    }

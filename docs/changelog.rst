.. _changelog:

=========
CHANGELOG
=========

1.2
===

* added a `joined_independently` signal
* refactored logic that existed in signal receivers to model methods
* fixed bug in add invites functionality that would set everyone to have unlimited invites
* fixed bug in top off invites functionality that removed unlimited invites from those who had it


1.1
===

* added a set of views to handle managing invites via ajax


1.0
===

* translated templates
* replaced `remaining_invites` template tag with `invites_remaining` inclusion template tag
* invite view is now bootstrap-ajax compatible


0.4
===

* moved away from Pinax dependencies and to require django-user-accounts
* moved to Django 1.4


0.3
===

* fixed documentation bugs
* added stats.py for stat collection


0.2
===

* added ability to set default invite allocation for new users
* added ability to enable users to have unlimited invitations

0.1
===

* initial release

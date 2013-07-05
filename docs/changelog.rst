.. _changelog:

=========
CHANGELOG
=========

1.2
===

* Django 1.5 custom user model support
* BACKWARD INCOMPATIBILITY: removed the import of `kaleo.receivers` from `urls.py`
* added a `joined_independently` signal
* refactored logic that existed in signal receivers to model methods
* fixed bug in add invites functionality that would set everyone to have unlimited invites
* fixed bug in top off invites functionality that removed unlimited invites from those who had it

Backward Inccompatibilities
---------------------------

Importing things into `models.py` or `urls.py` that have nothing to do with either of those
modules has been a bit of a hack for awhile. Pinax is moving to a more explicit approach where
these things are hooked up at the project level. In fact, Pinax starter projects will support
`receivers.py` getting hooked up at runtime automatically through the use of a `startup.py`
modeule that has code that gets executed in the `wsgi.py` and `manage.py`.

See how it all works in this commit:

https://github.com/pinax/pinax-project-account/commit/364795cdd683574ab6a5093be34b9d47a3487bea


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

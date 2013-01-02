.. _management:

Management Commands
===================

add_invites
-----------

Adds invites to all users with 0 invites remaining.

    manage.py add_invites 10  # Adds 10 new invites to all users with 0 invites remaining


topoff_invites
--------------

Makes sure all users have at least a certain number of invites.

    manage.py topoff_invites 10  # Makes sure that all users have at least 10 invites

.. _signals:

Signals
=======

Both of these signals are sent from `JoinInvitation` and provides a
single keyword argument, `invitation` which is the relevant instance
of `JoinInvitation`.


kaleo.signals.invite_sent
^^^^^^^^^^^^^^^^^^^^^^^^^

This signal is sent immediately after the invitation is sent.


kaleo.signals.invite_accepted
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This signal is sent immediately after the acceptance of the invitation
has been processed.

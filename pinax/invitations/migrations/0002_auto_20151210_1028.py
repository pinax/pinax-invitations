# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_invitations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable("JoinInvitation", "pinax_invitations_joininvitation"),
        migrations.AlterModelTable("InvitationStat", "pinax_invitations_invitationstat"),
    ]

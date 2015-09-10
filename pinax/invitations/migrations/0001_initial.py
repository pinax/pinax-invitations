# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invites_sent', models.IntegerField(default=0)),
                ('invites_allocated', models.IntegerField(default=0)),
                ('invites_accepted', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JoinInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True)),
                ('sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, b'Sent'), (2, b'Accepted'), (3, b'Joined Independently')])),
                ('from_user', models.ForeignKey(related_name='invites_sent', to=settings.AUTH_USER_MODEL)),
                ('signup_code', models.OneToOneField(to='account.SignupCode')),
                ('to_user', models.ForeignKey(related_name='invites_received', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

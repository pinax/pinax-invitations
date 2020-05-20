![](http://pinaxproject.com/pinax-design/patches/pinax-invitations.svg)

# Pinax Invitations

[![](https://img.shields.io/pypi/v/pinax-invitations.svg)](https://pypi.python.org/pypi/pinax-invitations/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-invitations.svg)](https://circleci.com/gh/pinax/pinax-invitations)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-invitations.svg)](https://codecov.io/gh/pinax/pinax-invitations)
[![](https://img.shields.io/github/contributors/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Dependencies](#dependencies)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
  * [Signals](#signals)
  * [Management Commands](#management-commands)
  * [Views](#views)
  * [Templates](#templates)
* [Change Log](#change-log)
* [History](#history)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-invitations

### Overview

`pinax-invitations` is a site invitation app for Django.

#### Dependencies

* django-user-accounts
* django-appconf

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-invitations:

```shell
    $ pip install pinax-invitations
```

Add `pinax.invitations` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.invitations",
    ]
```

Add [settings](#settings) as needed to customize pinax-invitation’s default behavior for your website.

Add `pinax.invitations.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^invitations/", include("pinax.invitations.urls", namespace="pinax_invitations")),
    ]
```

### Usage

Integrating pinax-invitations into your project involves using template tags and wiring up javascript.
The invite form is intended to function via AJAX and as such returns JSON. Incorporate
[`eldarion-ajax`](https://github.com/eldarion/eldarion-ajax) for markup-based AJAX handling
that works out of the box. Note you can use another AJAX handling library if needed.

`pinax-theme-bootstrap` is a semi-optional dependency. The only reason it is required is
the included _invite_form.html renders the form through the as_bootstrap filter.
If you override this template in your project, you obviously remove this requirement in context of this app.

Get started by adding the following blocks to your templates to expose an invite form
and display to the user a list of who they have invited:

```django
{% load pinax_invitations_tags %}

<div class="invites">
    {% invite_form request.user %}

    <div class="sent">
        <h3>Invitations Sent</h3>
        {% invites_sent request.user %}
    </div>
</div>
```

Then if you have an account bar somewhere at the top of your screen
which shows the user if they were logged in or not, you might include
this tag to show the number of invites remaining for a user:

```django
{% load pinax_invitations_tags %}

{% invites_remaining user %}
```

You’ll then need to include eldarion-ajax:

```django
<script>require('eldarion-ajax');</script>
```

### Settings

#### PINAX_INVITATIONS_DEFAULT_EXPIRATION

Defines the default expiration period for invitations in hours.
This setting is currently the only way to specify the expiration date of invitations.

Default: 168 (seven days)

#### PINAX_INVITATIONS_DEFAULT_INVITE_ALLOCATION

Defines the default number of invites that new users are allocated when they signup.
In order to enable unlimited invitations, set this to -1.

Default: 0

### Signals

These signals are sent from `JoinInvitation` and provides a single keyword argument, "invitation"
which is the relevant instance of `JoinInvitation`.

#### pinax_invitations.signals.invite_sent

Sent immediately after the invitation is sent.

#### pinax_invitations.signals.invite_accepted

Sent immediately after invitation acceptance has been processed.

#### pinax_invitations.joined_independently

Sent when someone signs up using the same email address that exists for an invitation
and they confirm that email address.

### Management Commands

#### add_invites

Adds invites to all users with 0 invites remaining.

```python
manage.py add_invites 10  # Adds 10 new invites to all users with 0 invites remaining
```

#### infinite_invites

Gives all users unlimited invites.

```python
manage.py infinite_invites
```

#### topoff_invites

Ensures all users have at least a certain number of invites.

```python
manage.py topoff_invites 10  # Ensure all users have at least 10 invites
```

### Views

Four different views handle POSTs via AJAX with a single variable, `amount`.
These views help administrators manage invites from a front-end dashboard.
Responses sent from these views conform to [`eldarion-ajax`](https://github.com/eldarion/eldarion-ajax) markup-based standards.

All views require the user permission `pinax_invitations.manage_invites`.
The largest use case is already be covered in that any user with "staff" or "superuser" privileges
supersedes the need for this explicit permission.

#### topoff_all

Tops off all users with at least `amount` invites.

URL: `pinax_invitations:topoff_all`

Returns:

```javascript
{
    "inner-fragments": {
        ".invite-total": amount
    }
}
```

#### topoff_user

Tops off `{{ user.pk }}` with at least `amount` invites.

URL: `pinax_invitations:topoff_user user.pk`

Returns:

```javascript
{
    "html": amount
}
```

#### addto_all

Adds `number` invites to all users.

URL: `pinax_invitations:addto_all`

Returns:

```javascript
{
    "inner-fragments": {
        ".amount-added": amount
    }
}
```

#### addto_user

Adds `number` invites to `{{ user.pk }}`.

URL: `pinax_invitations:addto_user user.pk`

Returns:

```javascript
{
    "inner-fragments": {
        ".html": amount
    }
}
```

#### invite_stat

Returns a rendered pinax/invitations/_invite_stat.html fragment (supplied by the site developer)
to render an `InvitationStat` object for the `user.pk` provided to the template as the context variable `stat`.

The intended target for this view is an element with `data-refresh-url` (processed by eldarion-ajax).

URL: `pinax_invitations:invite_stat user.pk`

Returns:

```javascript
{
    "html": <rendered pinax/invitations/_invite_stat.html>  # provided by site developer
}
```

### Templates

`pinax-invitations` uses minimal template snippets rendered with template tags.

Default templates are provided by the `pinax-templates` app in the
[invitations](https://github.com/pinax/pinax-templates/tree/master/pinax/templates/templates/pinax/invitations)
section of that project.

Reference pinax-templates
[installation instructions](https://github.com/pinax/pinax-templates/blob/master/README.md#installation)
to include these templates in your project.

View live `pinax-templates` examples and source at [Pinax Templates](https://templates.pinaxproject.com/invitations/fragments/)!

#### Customizing Templates

Override the default `pinax-templates` templates by copying them into your project
subdirectory `pinax/invitations/` on the template path and modifying as needed.

For example if your project doesn't use Bootstrap, copy the desired templates
then remove Bootstrap and Font Awesome class names from your copies.
Remove class references like `class="btn btn-success"` and `class="icon icon-pencil"` as well as
`bootstrap` from the `{% load i18n bootstrap %}` statement.
Since `bootstrap` template tags and filters are no longer loaded, you'll also need to update
`{{ form|bootstrap }}` to `{{ form }}` since the "bootstrap" filter is no longer available.

#### `_invite_form.html`

A snippet that renders the invite form as well as a div to hold the contents
of the response from the form AJAX submission.

#### `_invited.html`

An unordered list of people you have invited that is linked to their profile when they join the site.

#### `_invites_remaining.html`

Fragment displays how many invites a particular user has.


## Change Log

### 7.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 6.1.2

* Replace deprecated `context_instance=RequestContext(r)` kwarg with `request=r` kwarg
* Add InviteView smoke tests
* Add form test

### 6.1.1

* Add django>=1.11 to requirements
* Update CI config
* Improve documentation markup

### 6.1.0

* Standardize documentation layout
* Drop Django v1.8, v1.10 support
* Copy documentation from `kaleo`

### 6.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.9 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 5.0.0

* update function views to CBVs

### 4.0.0 - 4.0.4

* package version updates

### 3.0.0

* Rename templatetag library from invitations_tags to pinax_invitations_tags

### 2.1.1

* Import error when importing login_required decorator

### 2.1.0

* Set default_app_config to point to the correct AppConfig
* Remove compat module that provided compatibility with old Django versions
* Pin to initial migration for django-user-accounts
* Bump DUA dependency
* Fix typo in setup.py url
* Remove placeholder text from readme and fix badges
* Add Django migrations
* Move templates into pinax-theme-bootstrap

### 2.0.0

* Initial release as `pinax-invitations`.


## History

Eldarion’s [`kaleo`](http://kaleo.readthedocs.io/en/latest/changelog.html) app was donated to Pinax and renamed `pinax-invitations`.


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).

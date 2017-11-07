![](http://pinaxproject.com/pinax-design/patches/pinax-invitations.svg)

# Pinax Invitations

[![](https://img.shields.io/pypi/v/pinax-invitations.svg)](https://pypi.python.org/pypi/pinax-invitations/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-invitations/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-invitations.svg)](https://circleci.com/gh/pinax/pinax-invitations)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-invitations.svg)](https://codecov.io/gh/pinax/pinax-invitations)
[![](https://img.shields.io/github/contributors/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-invitations.svg)](https://github.com/pinax/pinax-invitations/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


## pinax-invitations

`pinax-invitations` is a site invitation app for Django.


## Table of Contents

The `pinax-invitations` documentation is currently under construction. If you would like to help us write documentation, please join our Slack team and let us know! 

* [Change Log](#change-log)
* [About Pinax](#about-pinax)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)


## Installation

## Change Log

### 5.1.0

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

* Eldarion’s `kaleo` app was donated to Pinax and renamed `pinax-invitations`.


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

The Pinax documentation is available at http://pinaxproject.com/pinax/. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our [blog](http://blog.pinaxproject.com).


## Contribute

See [this blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/) including a video, or our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our [Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you [join our Pinax Slack team](http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our [Open Source and Self-Care blog post](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found [here](http://pinaxproject.com/pinax/code_of_conduct/). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.

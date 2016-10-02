#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'psu'
SITENAME = u'Mutable States'
COPYRIGHT = 'Copyright (c) 2013-2016'
SITEURL = 'http://mutable-states.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "./psu_tux"

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ["render_math"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#pages
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GOOGLE_ANALYTICS='UA-41781936-1'

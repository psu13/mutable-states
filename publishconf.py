#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'psu'
SITENAME = u'Mutable States'
COPYRIGHT = u'Copyright (c) 2003-2021'
SITEURL = 'http://mutable-states.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "./psu_tux"

STATIC_PATHS = ['math']
PLUGINS = ["render_math"]

#pages
DISPLAY_PAGES_ON_MENU = False

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

#publish only
FEED_ALL_ATOM=('feeds/all.atom.xml')
FEED_ALL_RSS =('feeds/all.rss.xml')
RELATIVE_URLS = False
FILES_TO_COPY=(('.htaccess', '.htaccess'),)
# Blogroll
LINKS =  ()

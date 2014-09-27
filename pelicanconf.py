#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michal Stolarczyk'
SITENAME = u'null log'
SITEURL = ''
GITHUB_USER = u'zeroDivisible'
DEFAULT_PAGINATION = 10
TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'en'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/zeroDivisible'),
        ('github', 'https://github.com/zeroDivisible'),)

# custom css
STATIC_PATHS = ['static', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}
CUSTOM_CSS = 'static/custom.css'

# visual related settings
THEME = './pelican-bootstrap/'
BOOTSTRAP_THEME = 'myunited'
PYGMENTS_STYLE = 'colorful'
BOOTSTRAP_NAVBAR_INVERSE = True


#PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

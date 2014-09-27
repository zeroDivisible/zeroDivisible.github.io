#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michal Stolarczyk'
SITENAME = u'null log'
SITEURL = 'http://zerodivisible.io'
RELATIVE_URLS = True
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

#url settings
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

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
HIDE_SIDEBAR = True


PYGMENTS_MD_OPTIONS = {'linenos': 'table'}

GOOGLE_ANALYTICS = 'UA-47086458-1'

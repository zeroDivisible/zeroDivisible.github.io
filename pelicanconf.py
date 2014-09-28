#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michal Stolarczyk'
SITENAME = u'a blog'
SITEURL = ''
#RELATIVE_URLS = True
#DEFAULT_PAGINATION = 10
TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'en'

PATH = 'content'

#url settings
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/zeroDivisible'),
        ('github', 'https://github.com/zeroDivisible'),)

# custom css
STATIC_PATHS = ['static', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# visual related settings
THEME = './pelican-bootstrap/'
BOOTSTRAP_THEME = 'myunited'
PYGMENTS_STYLE = 'colorful'
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = False
DISPLAY_BREADCRUMBS = False
USE_PAGER = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

GOOGLE_ANALYTICS = 'UA-47086458-1'


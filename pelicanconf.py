#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'akimach'
SITENAME = u'akimach.note'
SITEURL = 'https://akimach.github.io/note'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

SITENAME = 'akimach.note'
SITETITLE = 'akimach.note'

GOOGLE_ANALYTICS = 'UA-109210790-1'

FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/profile.png'

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Blog(en)', 'https://medium.com/@akimach'),
         ('Blog(ja)', 'http://akimacho.hatenablog.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/akimach'),
          ('twitter', 'https://twitter.com/ki_macho'),
          ('rss', '/feeds/all.atom.xml'),)

ADD_THIS_ID = 'ra-5a002ebf95b44583'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Theme
THEME = '/Users/akimach/pelican-themes/Flex'

COPYRIGHT_YEAR = 2016
ROBOTS = 'index, follow'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
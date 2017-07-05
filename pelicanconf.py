#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'潘俊xi'
SITENAME = u'潘俊xi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/panjunjun'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', '#'),
    # ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10
# BLOG_AUTHORS = dict(
#     panjunxi="潘俊xi"
# )
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# THEME_STATIC_DIR = './theme/pelican-themes'
THEME = "theme/pelican-themes/zurb-F5-basic"
# DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 10
# DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 10
# LICENSE = "nothing"
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']

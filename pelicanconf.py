#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"潘俊xi"
SITENAME = u"潘俊xi"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = u"zh"
PAGE_LANG_URL = "pages/{slug}-{lang}.html"


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


LINKS = (
    ("Github", "https://github.com/panjunjun"),
)

SOCIAL = (
    ("LinkedIn", "http://www.linkedin.com/in/%E4%BF%8A%E4%BF%8A-%E6%BD%98-a68132a8/"),
)

DEFAULT_PAGINATION = 10

THEME = "theme/pelican-themes/zurb-F5-basic"

MARKUP = ("md", "ipynb")
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["ipynb.markup"]
IGNORE_FILES = [".ipynb_checkpoints"]
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"

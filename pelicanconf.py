#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import expanduser

AUTHOR = u'Robert Kirby and Andreas Kloeckner'
SITENAME = u'Transform-to-perform: Languages, algorithms, and code transformations for high-performance FEM'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Robert Kirby', 'https://www.baylor.edu/Math/index.php?id=90540'),
         ('Andreas Klöckner', 'https://andreask.cs.illinois.edu/'),
         ('NSF', 'http://nsf.gov'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = expanduser("~/web/pelican-bootstrap3")

ABOUT = """
    <p>
    A site about Rob's and Andreas's NSF project.
    </p>
    """



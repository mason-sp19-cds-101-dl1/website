# -*- coding: utf-8 -*-
"""Pelican publishing settings for CDS 101 website."""

from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = "http://sp19-dl1.cds101.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

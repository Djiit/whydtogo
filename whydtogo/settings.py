# -*- coding: utf8 -*-
""" Whydtogo Settings module."""

# Default output format
YDL_PARAMS = {
    'outtmpl': '%(title)s.%(ext)s',
}

#!!DEV Use Browser ? (Selenium)
USE_BROWSER = False

# Whyd root URL
ROOT_URL = 'https://whyd.com'

# CSS classes used to target track links.
CLASSES = [
    'via youtube',
    'via soundcloud',
]

# CSS class used to target "Load More" button. ##UNUSED
LOAD_MORE = 'btnLoadMore'


# Enable DEBUG mode. Usefull for development.
DEBUG = False

# Display the browser window.
DISPLAY = DEBUG

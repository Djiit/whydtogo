""" Whydtogo Settings module."""

# Default output format
YDL_PARAMS = {
    'outtmpl': '%(title)s.%(ext)s',
}

#!!DEV Use Browser ? (Selenium)
USE_BROWSER = False

# Classes to look for.
CLASSES = [
    'via youtube',
    'via soundcloud',
]

# Used to target "Load More" button.
LOAD_MORE = 'btnLoadMore'

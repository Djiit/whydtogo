# -*- coding: utf8 -*-
"""Whyd To Go - Take your Whyd playlists away.

Usage:
  whydtogo user <username> [-l, -d, -x]
  whydtogo playlist <url>... [-l, -d, -x]

Options:
  -h --help          Show this message
  <username>         Username to scrap
  <url>              URL to parse
  -l --list          Print tracks links; do not download them
  -d --debug         Enable debug mode
  -x --extratracks   Use Ghost.py browser to parse more than 20 tracks
"""

__version__ = "0.2.0"
__author__ = "Julien Tanay"

import logging

from docopt import docopt

from scraper import Scraper
import settings


def main():
    """ Main Whyd To Go CLI entry point."""
    args = docopt(__doc__)

    if args['--extratracks']:
        settings.USE_BROWSER = True

    if args['--debug']:
        settings.DEBUG = True

    if settings.DEBUG:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

    wtg = Scraper(settings)

    if args['user']:
        for url in wtg.get_playlists(args['<username>']):
            title = wtg.get_playlist_title(url)
            print(title)

            for link in wtg.get_links(url):
                if not args['--list']:
                    wtg.download(link, title)
                else:
                    print(link)

    elif args['playlist']:
        for url in args['<url>']:
            title = wtg.get_playlist_title(url)
            print(title)

            for link in wtg.get_links(url):
                if not args['--list']:
                    wtg.download(link, title)
                else:
                    print(link)

if __name__ == '__main__':
    main()

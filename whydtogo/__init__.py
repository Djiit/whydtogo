# -*- coding: utf8 -*-
"""Whyd To Go - Take your Whyd playlists away.

Usage:
  whydtogo user <username> [-l, -d]
  whydtogo playlist <url>... [-l, -d]

Options:
  -h --help          Show this message
  -l --list          Print tracks links; do not download them.
  -d --debug         Enable debug mode
  <username>         Username to scrap.
  <url>              URL to parse.

JT - 2014
"""

__version__ = "0.1.2"
__author__ = "Julien Tanay"

import logging

from docopt import docopt

from scraper import Scraper
import settings


def main():
    """ Main Whyd To Go CLI entry point."""
    args = docopt(__doc__)
    wtg = Scraper(settings)

    if args['--debug']:
        settings.DEBUG = True

    if settings.DEBUG:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

    if args['user']:
        for url in wtg.get_playlists(args['<username>']):
            title = wtg.get_playlist_title(url)
            print(title)

            for link in wtg.get_links(url):
                if not args['--list']:
                    wtg.download(link, wtg.get_playlist_title())
                else:
                    print(link)

    elif args['playlist']:
        for url in args['<url>']:
            title = wtg.get_playlist_title(url)
            print(title)

            for link in wtg.get_links(url):
                if not args['--list']:
                    wtg.download(link, wtg.get_playlist_title())
                else:
                    print(link)

if __name__ == '__main__':
    main()

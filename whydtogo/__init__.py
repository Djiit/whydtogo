# -*- coding: utf8 -*-
"""Whyd To Go - Take your Whyd playlists away.

Usage:
  whydtogo user <username>...
  whydtogo playlist <url>...

Options:
  -h --help          Show this message
  -d --debug         Enable debug mode
  <username>         Username to scrap.
  <url>              URL to parse.

JT - 2014
"""

__version__ = "0.1.1"
__author__ = "Julien Tanay"

from docopt import docopt

from scraper import Scraper
import settings


def main():
    """ Main Whyd To Go CLI entry point."""
    args = docopt(__doc__)
    wtg = Scraper(settings)
    for url in args['<url>']:
        for link in wtg.get_links(url):
            wtg.download(link, wtg.get_playlist_title())


if __name__ == '__main__':
    main()

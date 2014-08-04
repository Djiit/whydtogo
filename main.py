"""Whyd to go - Take your Whyd playlists away.

Usage:
  whydtogo.py user <username>...
  whydtogo.py playlist <url>...

Options:
  -h --help          Show this message
  <username>         Username to scrap.
  <url>              URL to parse.

JT - 2014
"""

from docopt import docopt

from whydtogo.scraper import Scraper
from whydtogo.settings import settings


def main():
    """ Main Whydtogo CLI entry point."""
    args = docopt(__doc__)
    wtg = Scraper(settings)
    for url in args['<url>']:
        for link in wtg.get_links(url):
            wtg.download(link, wtg.get_playlist_title(url))

if __name__ == '__main__':
    main()

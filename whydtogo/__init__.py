# -*- coding: utf8 -*-
"""Whyd To Go - Take your Whyd playlists away.

Usage:
  whydtogo user <username> [-s|-t|-l] [-p, -d]
  whydtogo playlist <url>... [-p, -d]

Options:
  -h --help          Show this message
  <username>         Username to scrap
  <url>              URL to parse
  -t --total        Fetch all user tracks (caution!)
  -s --stream        Fetch user stream (last tracks)
  -l --likes         Fetch user likes (last tracks)
  -p --print         Just print tracks, do not download them
  -d --debug         Enable debug mode
"""

import logging

from docopt import docopt

from scraper import WhydScraper


__author__ = "Julien Tanay"

__version__ = "0.3.0"
VERSION = __version__


def main():
    """ Main Whyd To Go CLI entry point."""
    args = docopt(__doc__)

    if args['--debug']:
        logging.getLogger().setLevel(logging.DEBUG)

    ws = WhydScraper()
    if args['user']:
        if args['--likes']:
            tracklist = ws.get_user_likes(args['<username>'])
            for track in tracklist:
                ws.download(
                    track['url'],
                    outdir='{user}_likes'.format(user=args['<username>']),
                    dry_run=args['--print'])

        elif args['--stream']:
            tracklist = ws.get_user_stream(args['<username>'])
            for track in tracklist:
                ws.download(
                    track['url'],
                    outdir=args['<username>'],
                    dry_run=args['--print'])

        elif args['--total']:
            tracklist = ws.get_user_stream(args['<username>'], limit='3000')
            for track in tracklist:
                    ws.download(
                        track['url'],
                        outdir=args['<username>'],
                        dry_run=args['--print'])

        else:
            for playlist_id in ws.scrap_playlists(args['<username>']):
                playlist = ws.get_playlist_by_id(
                    args['<username>'], playlist_id)

                for track in playlist:
                        ws.download(
                            track['url'],
                            outdir=track['playlist'],
                            dry_run=args['--print'])

    elif args['playlist']:
        for url in args['<url>']:
            playlist = ws.get_playlist_by_url(url)

            for track in playlist:
                ws.download(
                    track['url'],
                    outdir=track['playlist'],
                    dry_run=args['--print'])


if __name__ == '__main__':
    main()

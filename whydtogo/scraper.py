# -*- coding: utf8 -*-
"""Scraper class used to retrieve Whyd source links and download audio tracks.
"""

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

import logging
import os
from time import sleep

from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
from ghost import Ghost
from ghost.ghost import TimeoutError
# ghost = Ghost()
# page, extra_resources = ghost.open("http://jeanphix.me")
# assert page.http_status==200 and 'jeanphix' in ghost.content


class Scraper(object):

    def __init__(self, settings):
        self.settings = settings
        self.ydl = YoutubeDL(self.settings.YDL_PARAMS)
        self.ydl.add_default_info_extractors()
        self.use_browser = self.settings.USE_BROWSER
        if self.use_browser:
            self.browser = Ghost(display=self.settings.DISPLAY)

    def _make_soup(self, url):
        """ Helper to make a BeautifulSoup object."""
        try:
            if self.use_browser:
                self.browser.open(url)
                return BeautifulSoup(self.browser.content)
            else:
                return BeautifulSoup(urlopen(url).read())
        except ValueError:
            logging.warning('The URL you provided is not valid : "%s"' % url)
            return None

    def get_playlists(self, username):
        """ Récupère les playlists d'un utilisateur.

            :param username: Nom d'utilisateur.
        """
        playlists = []
        soup = self._make_soup('https://whyd.com/' + username + '/playlists')
        # TODO
        return playlists

    def get_links(self, url):
        """ Récupère les liens des tracks d'une page de playlist.

            :param url: URL de la playlist à parser.
        """
        links = []
        soup = self._make_soup(url)
        total_tracks = int(soup.find('div', class_='postsHeader').span.text.split()[0])
        print(total_tracks, total_tracks // 20)

        try:
            for _ in range(total_tracks // 20):
                self.browser.evaluate('loadMore();', expect_loading=True)
                sleep(2)
        except TimeoutError:
            pass

        soup = BeautifulSoup(self.browser.content)
        if soup:
            for class_name in self.settings.CLASSES:
                for tag in soup.find_all('a', class_=class_name):
                    links.append(tag['href'].split('#')[0])
        print(len(links), links)
        return links

    def get_playlist_title(self):
        soup = BeautifulSoup(self.browser.content)
        if soup:
            return soup.find('h1').string

    def download(self, url, outdir):
        """ Télécharge la version audio d'un lien.

            :param url: Lien vers la track.
            :param outdir: Dossier de destination.
        """
        try:
            os.mkdir(outdir)
            logging.debug('outdir created.')
        except:
            logging.debug('outdir already exists, skipping creation.')
        self.ydl.params['outtmpl'] = outdir + '/%(title)s.%(ext)s"'
        return self.ydl.extract_info(url, download=False)

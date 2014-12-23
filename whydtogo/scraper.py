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
from youtube_dl.utils import DownloadError

try:
    from ghost import Ghost
    from ghost.ghost import TimeoutError
except:
    logging.info('Ghost implementation not found and/or \
                  PyQt4/Pyside is missing.')


class Scraper(object):

    def __init__(self, settings):
        self.settings = settings
        self.ydl = YoutubeDL(self.settings.YDL_PARAMS)
        self.ydl.add_default_info_extractors()
        if self.settings.USE_BROWSER:
            self.browser = Ghost(display=self.settings.DISPLAY,
                                 wait_timeout=3600,
                                 java_enabled=False,
                                 plugins_enabled=False,
                                 download_images=False)

    def _make_soup(self, url):
        """ Helper to make a BeautifulSoup object.

            :param url: URL de la page à parser.
        """
        try:
            if self.settings.USE_BROWSER:
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
        pl_tag = soup.find('ul', id='playlists')
        for li in pl_tag.find_all('li'):
            playlists.append(self.settings.ROOT_URL + li.a['href'])
        return playlists

    def get_links(self, url):
        """ Récupère les liens des tracks d'une page de playlist.

            :param url: URL de la playlist à parser.
        """
        links = []
        soup = self._make_soup(url)

        if self.settings.USE_BROWSER:
            soup = self._load_more(soup)

        if soup:
            for class_name in self.settings.CLASSES:
                for tag in soup.find_all('a', class_=class_name):
                    links.append(tag['href'].split('#')[0])
        return links

    def get_playlist_title(self, url=None):
        if url:
            soup = BeautifulSoup(urlopen(url).read())
        else:
            soup = BeautifulSoup(self.browser.content)
        if soup:
            return soup.find('h1').string

    def download(self, url, outdir):
        """ Télécharge la version audio d'un lien.

            :param url: Lien vers la track.
            :param outdir: Dossier de destination.
        """
        # output root folder
        try:
            os.mkdir('output')
        except OSError:
            pass
        # playlist specific folder
        try:
            os.mkdir('output/%s' % outdir)
            logging.info('output/%s created.' % outdir)
        except OSError:
            logging.info('output directory already exists, skipping creation.')

        self.ydl.params['outtmpl'] = 'output/' + outdir + '/%(title)s.%(ext)s"'
        try:
            self.ydl.extract_info(url, download=True)
        except DownloadError as e:
            logging.info(e)
            return 

    def _load_more(self, soup):
        """ Evaluate 'loadMore()' in the Ghost.py browser to get all the traks."""
        total_tracks = int(soup.find('div', class_='postsHeader')
                               .span.text.split()[0])
        logging.info('Found %d tracks, loading %d more times.'
                     % (total_tracks, total_tracks // 20))
        try:
            for _ in range(total_tracks // 20):
                self.browser.evaluate('loadMore();', expect_loading=True)
                sleep(2)
        except TimeoutError:
            pass
        return BeautifulSoup(self.browser.content)

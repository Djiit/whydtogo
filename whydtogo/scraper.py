"""Scraper class used to retrieve Whyd source links and download audio tracks.
"""

from urllib.request import urlopen
import logging
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

class Scraper(object):

    def __init__(self, settings):
        self.settings = settings
        self.ydl = YoutubeDL(self.settings.YDL_PARAMS)
        self.ydl.add_default_info_extractors()
        self.use_browser = settings.USE_BROWSER
        if self.use_browser:
            self.browser = webdriver.PhantomJS()

    def _make_soup(self, url):
        """ Helper to make a BeautifulSoup object."""
        if self.use_browser:
            self.browser.get(url)
            return BeautifulSoup(self.browser.page_source)
        else:
            return BeautifulSoup(urlopen(url).read())

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
        # lmb = self.browser.find_element_by_class_name(self.settings.LOAD_MORE)
        # print(lmb)
        for class_name in self.settings.CLASSES:
            for tag in soup.find_all('a', class_=class_name):
                links.append(tag['href'].split('#')[0])
        return links

    def get_playlist_title(self, url):
        soup = self._make_soup(url)
        return soup.find('h1').string

    def download(self, url, outdir):
        """ Lance un process youtube-dl et télécharge la version audio d'un lien.

            :param url: Lien vers la track.
            :param outdir: Dossier de destination.
        """
        try:
            os.mkdir(outdir)
            logging.debug('outdir created.')
        except:
            logging.debug('outdir already exists, skipping creation.')
        self.ydl.params['outtmpl'] = outdir + '/%(title)s.%(ext)s"'
        return self.ydl.extract_info(url, download=True)

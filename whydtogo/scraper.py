"""Scraper class used to retrieve Whyd source links and download audio tracks.
"""

from urllib.request import urlopen
from subprocess import call
import logging
import os

import bs4 as BeautifulSoup


class Scraper(object):
    def __init__(self, settings):
        self.settings = settings

    def get_playlists(self,username):
        """ Récupère les playlists d'un utilisateur.

            :param username: Nom d'utilisateur.
        """
        playlists = []
        html = urlopen('https://whyd.com/'+username+'/playlists').read()
        soup = BeautifulSoup.BeautifulSoup(html)
        # TODO
        return playlists

    def get_links(self, url):
        """ Récupère les liens des tracks d'une page de playlist.

            :param url: URL de la playlist à parser.
        """
        links = []
        html = urlopen(url).read()
        soup = BeautifulSoup.BeautifulSoup(html)
        for class_name in self.settings['CLASSES']:
            for tag in soup.find_all('a',class_=class_name):
                links.append(tag['href'].split('#')[0])
        return links

    def get_playlist_title(self,url):
        html = urlopen(url).read()
        soup = BeautifulSoup.BeautifulSoup(html)
        return soup.find('h1').string

    def download(self, url, outdir):
        """ Lance un process youtube-dl et télécharge la version audio d'un lien.

            :param url: Lien vers la track.
            :param outdir: Dossier de destination.
        """
        try:
            os.mkdir(outdir)
        except:
            pass
        return call('youtube-dl ' + url + ' -x -o "'+ outdir + '/%(title)s.%(ext)s')

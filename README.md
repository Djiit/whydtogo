# Whyd to go

[![Build Status](https://travis-ci.org/Djiit/whydtogo.svg)](https://travis-ci.org/Djiit/whydtogo) [![Coverage Status](https://coveralls.io/repos/Djiit/whydtogo/badge.svg)](https://coveralls.io/r/Djiit/whydtogo)

## About

"Take your Whyd playlists away."

This is a very simple comand-line wrapper around youtube-dl for Whyd using BeautifulSoup4, requests and docopt.

This project is still unstable. Many thanks to the [Whyd](https://whyd.com) for their support.

## Usage

Check the built-in help message : `whydtogo --help`

For development usage use `python whydtogo/__init__.py --help`

Don't want to install anything ? Use this automatically generated [Docker image](https://registry.hub.docker.com/u/djiit/whydtogo/) :

```bash
docker run djiit/whydtogo
```

## Installation (all platforms)

You will need (obviously) Python 3.X and pip. Python 3.4 comes bundled with pip.
For Python 3.2 or 3.3, check how to install pip here : https://pip.pypa.io/en/latest/installing.html.

Optional : to extract audio from YouTube videos, you will also need avconv of ffmpeg (check how to download ffmpeg here : https://www.ffmpeg.org/download.html)

In a terminal, type :

```bash
git clone git@github.com:Djiit/whydtogo.git
cd whydtogo
pip install -r requirements.txt
```

To install WhydToGo on your system and use it as a standalone CLI program :

```bash
python setup.py install
```

## License

See [LICENSE](./LICENSE)

# Whyd to go

"Take your Whyd playlists away."

This is a very cheap and simple CLI wrapper around youtube-dl for Whyd using BeautifulSoup4 and docopt.

## Usage

Check the built-in help message : `whydtogo --help`

For development usage use `python whydtogo/__init__.py --help`

## Dependencies

You will need (obviously) Python 3.X and pip. Python 3.4 comes bundled with pip.
For Python 3.2 or 3.3, check how to install pip here : https://pip.pypa.io/en/latest/installing.html .

### Windows

Install PySide binaries from http://pyside.readthedocs.org/en/latest/installing/windows.html

### Linux

Build PySide from sources (http://pyside.readthedocs.org/en/latest/building/linux.html)

## Installation (all platforms)

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

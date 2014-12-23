# Whyd to go

"Take your Whyd playlists away."

This is a very cheap and simple CLI wrapper around youtube-dl for Whyd using BeautifulSoup4 and docopt.

## Usage

Check the built-in help message : `whydtogo --help`

For development usage use `whydtogo/__init__.py --help`

## Installation

### Windows

#### Dependencies

Install PySide binaries from http://pyside.readthedocs.org/en/latest/installing/windows.html

Then, in a terminal :

```bash
git clone git@github.com:Djiit/whydtogo.git
cd whydtogo
pip install -r requirements.txt
```

#### Binaries

To use Whydtogo as a CLI program, run :
```bash
python setup.py install
```

### Linux

Build PySide from sources (http://pyside.readthedocs.org/en/latest/building/linux.html)

Then, in a terminal :

```bash
git clone git@github.com:Djiit/whydtogo.git
cd whydtogo
python setup.py install
```

## License

See [LICENSE](./LICENSE)

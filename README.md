<h1 align="center">
svart
</h1>
<p align="center">
Change between dark/light mode depending on the ambient light intensity
<img src="images/preview.gif" align="center">
<br>

## Installation

### Install using `pip`
```console
$ python3 -m pip install --user svart
```

### Install using `git`
```
$ git clone git@github.com:sdushantha/svart.git
$ cd svart
$ python3 setup.py install
```

## Usage
```console
$ svart --help
usage: svart [options]

positional arguments:
  ambient               Dark mode when ambient light reaches this level (default: 1,100,000) (commas are not needed)

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v, --debug, -d
                        Show some information that might be useful during debugging
  --timeout TIMEOUT, -t TIMEOUT
                        Seconds between each check of the ambient level (default: 0)
  --version             Show version number
 ```

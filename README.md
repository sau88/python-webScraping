# python-webScraping
Get hotels prices from google by picking up arrival and departure dates



1. Install python 3.5 from 
https://www.python.org/downloads/

2. after installation go to terminal and type python hit enter...it shoul look like this

yking18@Zorin12:~$ python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

3. install pip (python package management system)


download pip source code from

https://pypi.org/project/pip/#files

download source "pip-19.1.1.tar.gz (1.3 MB)"

extract it

change dir path of terminal to extracted folder and look setup.py

run it by command "python setup.py"

3.1 check if pip install successfully

type "pip" in terminal and response should be like this


(virtual) yking18@Zorin12:~$ pip

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user
                              configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times
                              (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe,
                              (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and
                              the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is
                              available for download. Implied with --no-index.
  --no-color                  Suppress colored output


7. Install "virtual enviroment" create your project directory and activate virtual enviroment


4. Now Just install all dependencies required by code

pip install selenium

pip install bs4 # BeautifulSoup

5. Download Chrome drivers from http://chromedriver.chromium.org/downloads


(Note my machine is 32 bit and linux 32 bit world is near to
go obsolete....and google have stoped all supports for 32 bit linux so thats why 
i am using firefox , you might not need to import path for chrome drivers.)


install it....

6. There you go...you can now run main code by command "python google-hotels.py"






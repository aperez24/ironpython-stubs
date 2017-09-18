""" Stub Generator for IronPython

Extended script based on script developed by Gary Edwards at:
gitlab.com/reje/revit-python-stubs

This is uses a slightly modify version of generator3,
github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py

Iterates through a list of targeted assemblies and generates stub directories
for the namespaces using pycharm's generator3.

Note:
    Some files ended up too large for Jedi to handle and would cause
    memory errors and crashes - 1mb+ in a single files was enough to
    cause problems. To fix this, there is a separate module that creates
    a compressed version of the stubs, but it also split large file
    into separate files to deal with jedi.
    These directories will show up in the stubs as (X_parts)


MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico
"""

import sys
import os
import re
import json
import time
from pprint import pprint

from utils.docopt import docopt
from utils.logger import logger
from utils.helper import Timer
from default_settings import PATHS, BUILTINS, ASSEMBLIES, IN_REVIT
from make_stubs import make

__version__ = '1.0.0'
__doc__ = """
    IronPython-Stubs | {version}

    Usage:
      ironstubs
      ironstubs make <assembly-name> [-d --output-dir] [-o --overwrite] [--no-json]
      ironstubs make_all [-d --output-dir] [-o --overwrite] [--no-json]
      ironstubs --version

    Examples:
      ipy -m ironstubs RhinoCommon

    Options:
      --output-dir           Path of Output Directory [default: release\\stubs]
      -f <file>              Text file with list of assembly names
      --overwrite            Force Overwrite if stub already exists [default: False].
      --no-json              Don't write json file [default: False].
      -h, --help             Show this screen.

    """.format(version=__version__)

arguments = docopt(__doc__, version=__version__)
# logger.info(arguments)

# OPTIONS
option_assembly = arguments['<assembly-name>']
option_assembly_file = arguments['-f']
option_output_dir = arguments['--output-dir']
option_overwrite = arguments['--overwrite']
option_no_json = not arguments['--no-json']

PROJECT_DIR = os.getcwd()  # Must execute from project dir
PATHS, BUILTINS, ASSEMBLIES, IN_REVIT
[sys.path.append(p) for p in SYS_PATHS] # Add Paths

if arguments['make']:
    # timer = Timer()
    # print('Done: {} seconds'.format(timer.stop()))
if arguments['make_all']:
    make(option_output_dir, assemblies=None, builtins=None, overwrite=False):



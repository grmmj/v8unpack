__version__ = '0.7.8'

import sys

from .index import update_index
from .v8unpack import main, extract, build

if __name__ == '__main__':
    sys.exit(main())

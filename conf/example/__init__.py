import sys

if sys.platform in {'linux'}:
    from .nix import *
elif sys.platform.startswith('win'):
    from .windows import *
else:
    raise OSError("Unsupported os: {}".format(sys.platform))
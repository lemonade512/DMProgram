import nose
import sys, os

argv = sys.argv[:]
argv.append('--nocapture')

def main(*args, **kwargs):
    nose.run(argv=argv, *args, **kwargs)

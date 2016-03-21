#!/usr/bin/env python

from ..presenter import Connect4Engine
import getopt
import sys

class MainView:

    def __init__(self):
        options, args = getopt.getopt(sys.argv[1:], "")
        self.engine = None
        try:
            args = [int(x) for x in args]
        except ValueError:
            print 'Error parsing integer values.'
            return None
        if len(sys.argv) > 2:
            self.engine = Connect4Engine(args[0], args[1])
        else:
            print 'Not enough arguments!'

    def run(self):
        print self.engine.board

def main():
    main_view = MainView()
    if main_view.engine is not None:
        main_view.run()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

from ..presenter import Connect4Engine
import getopt
import sys

class MainView:

    def __init__(self):
        options, args = getopt.getopt(sys.argv[1:], "")
        args = [int(x) for x in args]
        if len(sys.argv) > 2:
            self.engine = Connect4Engine(args[0], args[1])

    def run(self):
        print self.engine.board

def main():
    main_view = MainView()
    main_view.run()

if __name__ == '__main__':
    main()

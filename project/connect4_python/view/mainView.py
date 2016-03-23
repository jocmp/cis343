#!/usr/bin/env python
import cPickle
import getopt
import sys
import signal
import re

from ..presenter import Connect4Engine

main_view = None

def signal_handler(signal, frame):
    global main_view
    main_view.save_state()
    sys.exit(0)

def main():
    global main_view
    main_view = MainView()
    signal.signal(signal.SIGINT, signal_handler)
    main_view.run()

class MainView:

    SAVE_FILENAME = "connect4_python/c4_save"
    __game_in_session = False

    def __init__(self):
        options, args = getopt.getopt(sys.argv[1:], "")
        self.engine = None
        self.engine = load_state()
        if self.engine is None:
            return
        try:
            args = [int(x) for x in args]
        except ValueError:
            print 'Error parsing integer values.'
            return None
        if len(args) > 2:
            self.engine = Connect4Engine(args[0], args[1])
        else:
            print 'Not enough arguments!'

    def save_state(self):
        try:
            save_file = open(MainView.SAVE_FILENAME, 'w')
        except IOError:
            print "Error: Write permissions are not enabled for " \
            + file_cant_open
        except OSError:
            print "Error: Write permissions are not enabled for " \
            + file_cant_open
        try:
            cPickle.dump(self.engine, save_file)
        except PicklingError:
            print "Couldn't pickle game."
        save_file.close
        return True

    def load_state(self):
        try:
            save_file = open(MainView.SAVE_FILENAME, 'r')
        except IOError:
            print "Error: Read permissions are not enabled for "\
            + file_cant_open
        except OSError:
            print "Error: Read permissions are not enabled for "\
            + file_cant_open
        saved_game = None
        try:
            saved_game = cPickle.load(save_file)
        except UnpicklingError:
            print "Couldn't unpickle game."
        return saved_game

    def print_winner(self, winner):
        if winner < 2:
            print "{w}".format(winner + 1) + "\n"
        else:
            print "Cat's game!\n"

    def run(self):
        change_player = lambda p: 1 if p == 0 else 0
        valid_input = lambda n: re.match('\d', str(n))
        MainView.game_in_session = True
        win = -1
        current_player = 0
        while MainView.game_in_session:
            print "Ready player " + str(current_player + 1)
            try:
                column = input("Enter column: ")
            except SyntaxError:
                continue
            placed =  self.engine.place_token(current_player, column)
            if placed < 0:
                print "\nCouldn't place token at column "\
                 + str(column) + "\n\n"
                continue
            print self.engine.board
            current_player = change_player(current_player)
            win = self.engine.winner()
            if win > 0:
                game_in_session = False
                break
        self.print_winner(win)

if __name__ == '__main__':
    main()

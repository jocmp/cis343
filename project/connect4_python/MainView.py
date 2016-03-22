#!/usr/bin/env python
import cPickle
import getopt
import os
import sys
import signal
import re

from Connect4Engine import Connect4Engine

main_view = None

def signal_handler(signal, frame):
    global main_view
    print "\nKeyboard interrupt.\n"
    if main_view.game_in_session:
        print "\nSaving game...\n"
        main_view.save_state()
    sys.exit(0)

def main():
    global main_view
    main_view = MainView()
    signal.signal(signal.SIGINT, signal_handler)
    if not (main_view.engine is None):
        main_view.run()
    else:
        return

class MainView:

    SAVE_FILENAME = "c4_save"
    game_in_session = False

    def __init__(self):
        options, args = getopt.getopt(sys.argv[1:], "")
        self.engine = self.load_state()
        answer = 'n'
        try:
            args = [int(x) for x in args]
        except ValueError:
            print 'Error parsing integer values.'
            return
        # Ask to load game
        if not (self.engine is None):
            try:
                answer = raw_input("Saved game found. Do you want to continue " \
                        + "playing? (y/n) ");
            except KeyboardInterrupt:
                return
            except NameError:
                print answer
        if answer == 'y':
            if len(args) > 2:
                print "New game: "
                self.engine = Connect4Engine(args[0], args[1], args[2])
            else:
                print 'Not enough arguments!'
                os.remove(MainView.SAVE_FILENAME)
                self.engine = None
                return
        print self.engine.board

    def save_state(self):
        save_file = None
        try:
            save_file = open(MainView.SAVE_FILENAME, 'w')
        except IOError:
            print "Error: Write permissions are not enabled for " \
            + MainView.SAVE_FILENAME
        cPickle.dump(self.engine, save_file)
        if not (save_file is None):
            save_file.close
        return True

    def load_state(self):
        save_file = None
        try:
            save_file = open(MainView.SAVE_FILENAME, 'r')
        except IOError:
            print "Error: Read permissions are not enabled for "\
            + MainView.SAVE_FILENAME
        if not (save_file is None):
            save_file.close
        return cPickle.load(save_file)

    def print_winner(self, winner):
        if winner < 2:
            print "Player " + str(winner + 1) + " wins!"
        else:
            print "Cat's game!\n"

    def run(self):
        change_player = lambda p: 1 if p == 0 else 0
        valid_input = lambda n: re.match('\d', str(n))
        MainView.game_in_session = True
        win = -1
        current_player = 0
        column = -1
        while MainView.game_in_session:
            print "Ready player " + str(current_player + 1)
            try:
                user_input = raw_input("Enter column: ")
            except KeyboardInterrupt:
                return
            except SyntaxError:
                continue
            if (user_input == "quit" or user_input == "exit"):
                print "\nSaving game...\n"
                self.save_state()
                game_in_session = False
                break
            elif not valid_input(user_input):
                continue
            column = int(user_input)
            placed = self.engine.place_token(current_player, column)
            if placed < 0:
                print "\nCouldn't place token at column "\
                 + user_input + "\n\n"
                continue
            print self.engine.board
            current_player = change_player(current_player)
            win = self.engine.winner()
            if win > 0:
                game_in_session = False
                break
        os.remove(MainView.SAVE_FILENAME)
        self.print_winner(win)

if __name__ == '__main__':
    main()

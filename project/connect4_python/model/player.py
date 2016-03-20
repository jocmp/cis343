#!/usr/bin/env python

class Player:
    __player_count = 0
    """docstring for Player"""

    def __init__(self):
        __player_count += 1
        self.id = __player_count

    def __str__(self):
        print "Player " + self.id

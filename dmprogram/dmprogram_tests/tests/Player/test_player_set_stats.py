#!/usr/bin/env python

# test_player_set_stats.py

from dmprogram.Player import Player
from nose.tools import *
import sys, os

class TestPlayer:

    @classmethod
    def setup_class(cls):
        print ''
        print os.path.split(__file__)[1]
        cls.test_player = Player(1,'test_player',2,3,4,5,6,7)

    def test_set_all_stats(self):
        new_stats = {
                'Name':'new_player',
                'AC':9,
                'Listen':9,
                'Spot':9,
                'Search':9,
                'Move_Silently':9,
                'Hide':9
                }
        self.test_player.SetStats(**new_stats)
        actual_stats = self.test_player.GetStats()
        for kw in new_stats:
            assert_equals(actual_stats[kw], new_stats[kw])

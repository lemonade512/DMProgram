#!/usr/bin/env python

from dmprogram.Player import Player
from nose.tools import *

class TestPlayer:

    def test_default_init(self):
        p1 = Player()
        default_expected_stats = {
                'ID':-1,
                'Name':'',
                'AC':-1,
                'Listen':-1,
                'Spot':-1,
                'Search':-1,
                'Move_Silently':-1,
                'Hide':-1
                }
        actual_stats = p1.GetStats()
        for kw in default_expected_stats:
            assert_equals(actual_stats[kw], default_expected_stats[kw])

    def test_player_init(self):
        p1 = Player(1,'test_player',1,1,1,1,1,1)
        expected_stats = {
                'ID':1,
                'Name':'test_player',
                'AC':1,
                'Listen':1,
                'Spot':1,
                'Search':1,
                'Move_Silently':1,
                'Hide':1
                }
        actual_stats = p1.GetStats()
        for kw in expected_stats:
            assert_equals(actual_stats[kw], expected_stats[kw])

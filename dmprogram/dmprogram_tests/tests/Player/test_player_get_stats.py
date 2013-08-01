#!/usr/bin/env python

# test_player_get_stats.py

from dmprogram.Player import Player
from nose.tools import *

class TestPlayer:

    @classmethod
    def setup_class(cls):
        cls.test_player = Player(1,'test_player',2,3,4,5,6,7)

    def test_get_all_stats(self):
        expected_stats = {
                'ID':1,
                'Name':'test_player',
                'AC':2,
                'Listen':3,
                'Spot':4,
                'Search':5,
                'Move_Silently':6,
                'Hide':7
                }
        assert_equals(self.test_player.GetStats(), expected_stats)

    def test_get_id_is_1(self):
        expected_id = 1
        assert_equals(self.test_player.GetID(), expected_id)

    def test_get_name_is_test_player(self):
        expected_name = 'test_player'
        assert_equals(self.test_player.GetName(), expected_name)

    def test_get_ac_is_2(self):
        expected_ac = 2
        assert_equals(self.test_player.GetAC(), expected_ac)

    def test_get_listen_is_3(self):
        expected_listen = 3
        assert_equals(self.test_player.GetListen(), expected_listen)

    def test_get_spoti_is_4(self):
        expected_spot = 4
        assert_equals(self.test_player.GetSpot(), expected_spot)

    def test_get_search_is_5(self):
        expected_search = 5
        assert_equals(self.test_player.GetSearch(), expected_search)

    def test_get_move_silently_is_6(self):
        expected_move_silently = 6
        assert_equals(self.test_player.GetMoveSilently(),
                      expected_move_silently)

    def test_get_hide_is_7(self):
        expected_hide = 7
        assert_equals(self.test_player.GetHide(), expected_hide)

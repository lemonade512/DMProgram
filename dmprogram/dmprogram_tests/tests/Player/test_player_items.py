#!/usr/bin/env python

# test_player_items.py

from dmprogram.Player import Player
from dmprogram.Item import Item
from nose.tools import *
import unittest
import sys, os

class TestPlayer(unittest.TestCase):

    @classmethod
    def setup_class(self):
        print('')
        print(os.path.split(__file__)[1])

    def setUp(self):
        self.test_player = Player(1,'test_player',2,3,4,5,6,7)

    def test_get_items_is_empty(self):
        assert_equals(self.test_player.GetItems(), [])

    def test_add_one_item(self):
        item = Item(1,1,'test_item','item description')
        self.test_player.AddItem(item)
        assert_equals(self.test_player.GetItems(), [item])

    def test_add_3_items(self):
        item1 = Item(1,1,'test_item1','description1')
        item2 = Item(2,1,'test_item2','description2')
        item3 = Item(2,1,'test_item3','description3')
        self.test_player.AddItems(item1, item2, item3)
        assert_equals(self.test_player.GetItems(), [item1,item2,item3])

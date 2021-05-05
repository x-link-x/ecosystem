import unittest
from src.river import *
from src.fish import *

class TestRiver( unittest.TestCase ):

    def setUp(self):
        self.fish_1 = Fish("Salmon")
        self.fish_2 = Fish("Cod")
        self.fish_3 = Fish("Haddock")
        self.river = River("Tay", [self.fish_1, self.fish_2, self.fish_3])
    
    def test_name(self):
        expected = "Tay"
        actual = self.river.name
        self.assertEqual( expected, actual )

    def test_fish_river_has_fish(self):
        expected = [self.fish_1, self.fish_2, self.fish_3]
        actual = self.river.fish
        self.assertEqual( expected, actual )

    def test_fish_count(self):
        expected = 3
        actual = self.river.fish_count()
        self.assertEqual( expected, actual )

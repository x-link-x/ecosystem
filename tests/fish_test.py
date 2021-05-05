import unittest
from src.fish import *

class TestFish( unittest.TestCase ):

    def setUp(self):
        self.fish_1 = Fish("Salmon")
        self.fish_2 = Fish("Cod")
        self.fish_3 = Fish("Haddock")

    def test_name(self):
        expected = "Cod"
        actual = self.fish_2.name
        self.assertEqual( expected, actual )
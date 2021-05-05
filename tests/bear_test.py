import unittest
from src.bear import *
from src.river import *
from src.fish import *

class TestBear( unittest.TestCase ):

    def setUp(self):
        self.bear = Bear("Fluffy", "polar")
        self.fish_1 = Fish("Salmon")
        self.fish_2 = Fish("Cod")
        self.fish_3 = Fish("Haddock")
        self.river = River("Tay", [self.fish_1, self.fish_2, self.fish_3])

    def test_name(self):
        expected = "Fluffy"
        actual = self.bear.name
        self.assertEqual( expected, actual )

    def test_type(self):
        expected = "polar"
        actual = self.bear.bear_type
        self.assertEqual( expected, actual )
        
    def test_stomach_empty(self):
        expected = []
        actual = self.bear.stomach
        self.assertEqual( expected, actual )

    def test_eat_fish(self):
        expected = [self.fish_3]
        # Act
        self.bear.bear_eats_fish(self.river)
        actual = self.bear.stomach
        self.assertEqual( expected, actual )
        self.assertEqual( [self.fish_1, self.fish_2], self.river.fish )
    
    def test_roar(self):
        expected = "ROOOOOAARRRRRR"
        actual = self.bear.roar()
        self.assertEqual( expected, actual )


    def test_food_count(self):
        expected = 0
        actual = self.bear.food_count()
        self.assertEqual( expected, actual )


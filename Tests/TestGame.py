from unittest import TestCase
from DiGraph import DiGraph
from game import game



class TestGame(TestCase):
    def test_isEdge(self):
        ga = game()
        g = DiGraph()
        g.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        g.add_edge(1, 2, 2)
        ga.graph = g
        self.assertTrue(ga.isEdge(1, 2))
        self.assertFalse(ga.isEdge(2, 1))

from unittest import TestCase
from GraphAlgo import GraphAlgo
from client_python import DiGraph

import os


class TestGraphAlgo(TestCase):

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/A0')
        self.assertEqual(g_algo.centerPoint(), (7, 6.806805834715163))

        algo1 = GraphAlgo()
        algo1.load_from_json('../data/A1')
        self.assertEqual(algo1.centerPoint(), (0, 6.323938666501508))

        algo2 = GraphAlgo()
        algo2.load_from_json('../data/A2')
        self.assertEqual(algo2.centerPoint(), (1, 7.699910325475899))

        algo3 = GraphAlgo()
        algo3.load_from_json('../data/A3')
        self.assertEqual(algo3.centerPoint(), (1, 5.247642190396624))

    def test_centerPoint(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/A0')
        self.assertEqual(g_algo.shortest_path(1, 9), (4.439215347640289, [1, 0, 10, 9]))

        algo1 = GraphAlgo()
        algo1.load_from_json('../data/A1')
        self.assertEqual(algo1.shortest_path(1, 9), (4.907094535151561, [1, 0, 10, 9]))




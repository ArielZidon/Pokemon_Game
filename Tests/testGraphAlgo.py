from unittest import TestCase
from client_python import DiGraph
from client_python import GraphAlgo
import os


class testGraphAlgo(TestCase):

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/A4.json')
        self.assertEqual(g_algo.centerPoint(),(6, 8.071366078651435))

    def test_TSP(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/A4.json')
        a = [1,2,3,4,5]
        self.assertEqual(g_algo.TSP([1,2,3,4,5]),([1, 2, 3, 4, 5], 6.132281193389314))

    def test_centerPoint(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/A4.json')
        self.assertEqual(g_algo.shortest_path(1,9),(9.363555395495794, [1, 2, 30, 31, 32, 7, 8, 9]))

    def test_save(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json('../data/1000Nodes.json')
        self.assertTrue(g_algo.save_to_json('test.json'))
        os.remove('test.json')



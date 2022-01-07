from unittest import TestCase
from DiGraph import DiGraph

class testDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        len_g = g.v_size()
        len_d = d.v_size()

        self.assertEqual(len_d, len_g)

    def test_e_size(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        g.add_edge(0, 1, 1)
        d.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        d.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        d.add_edge(2, 3, 3)
        g.add_edge(3, 4, 4)
        d.add_edge(3, 4, 4)

        len_g = g.e_size()
        len_d = d.e_size()


    def test_get_all_v(self):
        g = DiGraph()
        x = 1

        g.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        g.add_node(4, (5, 5))

        for node in g.get_all_v().keys():
            self.assertEqual(node, x)
            x += 1

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        g.add_edge(0, 1, 1)
        d.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        d.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        d.add_edge(2, 3, 3)
        g.add_edge(3, 4, 4)
        d.add_edge(3, 4, 4)

        self.assertEqual(d.all_in_edges_of_node(2), g.all_in_edges_of_node(2))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))

        g.add_edge(0, 1, 1)
        d.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        d.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        d.add_edge(2, 3, 3)


        self.assertEqual(d.all_out_edges_of_node(1), g.all_out_edges_of_node(1))

    def test_get_mc(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))

        self.assertEqual(d.mc, 3)
        self.assertEqual(g.mc, 4)
        self.assertEqual(g.mc, d.mc + 1)

    def test_add_edge(self):
        g = DiGraph()
        d = DiGraph()

        g.add_edge(0, 1, 1)
        d.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        d.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        d.add_edge(2, 3, 3)
        g.add_edge(3, 4, 4)
        d.add_edge(3, 4, 4)

        for edge in d, g:
            self.assertEqual(d.edges.keys(), g.edges.keys())

    def test_add_node(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        for node in d, g:
            self.assertEqual(d.nodes.keys(), g.nodes.keys())

    def test_remove_node(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        d.remove_node(3)
        g.remove_node(3)

        for node in d, g:
            self.assertEqual(d.nodes.keys(), g.nodes.keys())

    def test_remove_edge(self):
        g = DiGraph()
        d = DiGraph()

        g.add_node(1, (2, 2))
        d.add_node(1, (2, 2))
        g.add_node(2, (3, 3))
        d.add_node(2, (3, 3))
        g.add_node(3, (4, 4))
        d.add_node(3, (4, 4))
        g.add_node(4, (5, 5))
        d.add_node(4, (5, 5))

        g.add_edge(0, 1, 1)
        d.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        d.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        d.add_edge(2, 3, 3)
        g.add_edge(3, 4, 4)
        d.add_edge(3, 4, 4)

        g.remove_edge(2, 3)
        d.remove_edge(2, 3)

        for node in d, g:
            self.assertEqual(d.nodes.keys(), g.nodes.keys())

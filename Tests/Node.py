"""
Class Node
In this class we receive Node's value and create it.
Values: key - the id number of the node.
        pos - the geographical position values of where the node is located.
        out - the edges that goes out of the node.
        in - the edges that goes into the node.
"""


class Node:
    # constructor
    def __init__(self, key: int, pos: tuple) -> None:
        self.key = key
        self.pos = pos
        self.out = {}
        self.In = {}

    def __str__(self):
        return f'key = {self.key}, ' f'pos = {self.pos}'

    # String with node's values
    def __repr__(self) -> str:
        return f'key = {self.key}, ' f'pos = {self.pos}'




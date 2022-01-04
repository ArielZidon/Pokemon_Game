"""
This class represent an agent.
"Agent":
       {
        "id":0,
        "value":0.0,
        "src":0,
        "dest":1,
        "speed":1.0,
        "pos":"35.18753053591606,32.10378225882353,0.0"
        }
"""

from argoments import agent


class Agent(object):

    # constructor to init agent, getting arguments from Json file using the class "agent" in the file "argoments".

    def __init__(self, id_: int, value: float, src: int, dest: int, speed: float, pos: list):
        self.id_ = agent.id
        self.value = agent.value
        self.src = agent.src
        self.dest = agent.dest
        self.speed = agent.speed
        self.pos = agent.pos

    # getters and setters

    # get method for the id
    def get_id(self):
        return self.id_

    # set method for the id
    def set_id(self, x):
        self.id_ = x

    # get method for the value
    def get_value(self):
        return self.id_

    # set method for the value
    def set_value(self, x):
        self.value = x

    # get method for the src
    def get_src(self):
        return self.src

    # set method for the src
    def set_src(self, x):
        self.src = x

    # get method for the dest
    def get_dest(self):
        return self.dest

    # set method for the dest
    def set_dest(self, x):
        self.dest = x

    # get method for the speed
    def get_speed(self):
        return self.speed

    # set method for the id
    def set_speed(self, x):
        self.speed = x

    # get method for the pos
    def get_pos(self):
        return self.pos

    # set method for the pos
    def set_pos(self, x):
        self.pos = x

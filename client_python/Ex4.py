import subprocess
from game import game
from client import Client

"""sys.argv[1]"""
# default port
PORT = 6666
# server host
HOST = '127.0.0.1'
client = Client()
game = game()
client.start_connection(HOST, PORT)
client.add_agent("{\"id\":0}")

game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())

<<<<<<< HEAD
print(game.__dict__)
=======
print(game.__dict__)

client.start()
while client.is_running() == 'true':
    size = len(game.graph.nodes)
    for agent in game.agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % size
            client.choose_next_edge('{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())
    client.move()
    game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
    # gui.draw()
>>>>>>> af54fac5783418fbd1490ec680d7e87acca93d2d

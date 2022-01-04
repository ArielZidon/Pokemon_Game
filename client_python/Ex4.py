import subprocess
from game import game
from client import Client
from graphGame import *

"""sys.argv[1]"""
# default port
PORT = 6666
# server host
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)

game = game()
client.add_agent("{\"id\":0}")

game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
drow = graphGame(game)
client.start()

while client.is_running():
    game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
    drow.main()
    # for agent in game.agents:
    #     if agent.dest == -1:
    #         next_node = (agent.src - 1) % len(game.graph.nodes)
    #         client.choose_next_edge(
    #             '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
    #         ttl = client.time_to_end()
    #         print(ttl, client.get_info())
    # client.move()



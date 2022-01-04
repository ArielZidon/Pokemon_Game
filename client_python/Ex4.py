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

print(game.__dict__)
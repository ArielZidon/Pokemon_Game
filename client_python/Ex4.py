import subprocess
import sys

from game import game
from client import Client

"""sys.argv[1]"""
subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {0}'])
# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)
client.add_agent("{\"id\":0}")
game = game()
game.builder(client.get_pokemons(), client.get_agents(), client.get_graph())

print(game.__dict__)
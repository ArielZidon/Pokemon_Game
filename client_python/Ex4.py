from graphGame import *
from send_Agent import *
import time

"""sys.argv[1]"""
# default port
PORT = 6666
# server host
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)

game = game()
def addAgents():
    size = int(json.loads(client.get_info())["GameServer"]["agents"])
    for i in range(size):
        client.add_agent("{\"id\":" + str(i) + "}")
addAgents()
game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
drow = graphGame(game)
G = send_Agent(game)
client.start()

while client.is_running():
    game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
    ttl = int(client.time_to_end())
    move = client.get_info().split(",")
    move = move[2].split(":")[1]
    grade = client.get_info().split(",")
    grade = grade[3].split(":")[1]
    drow.main(move, int(ttl/1000), grade)
    # print(ttl, client.get_info())
    G.cmd(client)
    time.sleep(0.0448)
    client.move()

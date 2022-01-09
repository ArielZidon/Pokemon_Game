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
c = 9

size = int(json.loads(client.get_info())["GameServer"]["agents"])

"""
The function calculates the amount of 
agents and places them on the game board
"""
def add_agent():
    size = int(json.loads(client.get_info())["GameServer"]["agents"])
    for i in range(size):
        if size ==1:
            client.add_agent("{\"id\":" + str(c) + "}")
        else:
            client.add_agent("{\"id\":" + str(i) + "}")
add_agent()

game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
drow = graphGame(game)
G = send_Agent(game)
client.start()

t = 0
if (int(client.time_to_end())/1000)>30:
    t = 1

"""
In this loop the game actually runs when we know how long the 
game will be played and with how many agents we will play
"""

while client.is_running():
    game.up_to_serv(client.get_pokemons(), client.get_agents(), client.get_graph())
    ttl = int(client.time_to_end())
    move = client.get_info().split(",")
    move = move[2].split(":")[1]
    grade = client.get_info().split(",")
    grade = grade[3].split(":")[1]
    drow.main(move, int(ttl/1000), grade,size)
    print(ttl, client.get_info(),game.agents[0].speed)
    if size == 1:
        G.cmd_solo(client,t)
        client.move()
    else:
        G.cmd_group(client,t)
        client.move()
        for a in game.agents:
            if a.mode == 0:
                G.pick_pok_for_A(a,client)


    # 0 V - 100
    # 1 V - 437
    # 2 V - 161
    # 3 V - 853
    # 4 V - 219
    # 5 V - 573
    # 6 V - 79
    # 7 V - 286
    # 8 V - 125
    # 9 V - 458
    # 10 V - 181
    # 11 V - 1758
    # 12 V - 40
    # 13 V - 269
    # 14 V - 94
    # 15 V - 310

    # 314789264
    # 208494989
    # 207817529


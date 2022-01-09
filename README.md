![pokemon](https://user-images.githubusercontent.com/93203695/148101905-a5026eed-4ce7-497a-bc45-6dfe751d4a64.png)

# Pokemon Game - PY 
# About The Project
In this project we created a simple game, which is about catching pokemos.</br>
The game's purpose is to collect as many points as we can, while every pokemon has a different value of points.</br>
The pokemons are located on a directed weighted connected graph. </br>
Our task is to locate the agents at the graph in the best position we can (we chose to locate them on the center of the graph), and send them to catch the most suitable pokemons.</br>
The consideration of a suitable pokemon relies on many different parameters:
- The number of agent's moves it will take to get the pokemon.
  - It depends on the distance of the pokemon from the agent, which means the number of edges the agent needs to go and their weight.
- The value of the pokemon.
  - Every pokemon has it's own value.
- We have limited time and limited number of moves (10 moves per sec).
  - Which means we need to consider how to collect as many points as we can with this limitation.  


# The Creation Process
First of all, the directed weighted connected graph, the pokemons and the agents values are received in a Json format.</br>
The graph's paramenters are it's nodes and edges. Every node has id number, geographical position value, edges that goes out of the node, and edges that goes to the node.</br> 
The Agent's parameters are it's id number, it's value, it's source and destination, it's speed and it's position.</br>
The Pokemon's parameters are it's value, it's type and it's position.</br>
We read the Json file and create all the above. To do this we created the class "argoments", where we receive the pokemons and the agents from the Json and create them.</br>
In addition, we created the class "GraphAlgo" to load the graph from the Json file and to implement algorithms on it.</br>
We created the class "Node" which represents a node of the graph, and the class Digraph which represents a graph.<br/>

<p align="center">
<img src="https://user-images.githubusercontent.com/93203695/148563497-cb051da1-5cc2-4030-b855-cb11963f3176.gif" alt="Gif"  width="450" height="400">
</a>
</p>

# The game algorithm
## The cmd_solo
The program will call this action when it detects that there is one agent in the game,
The function will go through all the Pokemon and give the agent the most suitable Pokemon according to the parameters given by the Shortest Path algorithm.

## The cmd_group
The program will call this function when there is more than one dangerous, in this case the function will go over all the * Pokemon * and give the Pokemon the corresponding agent when at the end of the function we send the preferred agent to the same Pokemon, the other unsent agents will be passed to the "cmd_solo" function to get Pokemon.

# Graph's Algorithms
## Shortest Path
Finds the shortest path in the graph between any 2 nodes we want. (Receives source node and destination node)

## Center
Finds the node with the smallest trajectory value toward all other graphite nodes.

### Dijkstra
dijkstra algorithm. https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# UML Diagram

![diagram-17363877052811065234](https://user-images.githubusercontent.com/93203695/148650907-a490945f-a800-4649-a439-005c9713a71a.png)


# Getting Started

<p align="center">
<img src="https://user-images.githubusercontent.com/93203695/148564696-3d332218-8a00-4bcb-ba31-2b8c43a0d59d.gif" alt="Gif"  width="600" height="400">
</a>
</p>

## Installation
In order to install the program you need to follow these steps:
- Download/clone the project from git.
- Extract the downloaded zip file.
- Open the project in Python environment workspace (we used PyCharm).
  - Note(!!!): __Download the library pygame__.
- Now that you have installed the project,
follow the next section to understand how to use the program.

## Usage
In order to run the program follow these steps:
- Open a new Terminal (if you use PyCharm, open the terminal at the lower toolbar)
- Write the command : java -jar Ex4_Server_v0.0.jar "Case number"
  - At the "Case number" just write a number between 0-15 (without the """)
  - Press Enter, now the server is up.
  - Run class Ex4
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/93203695/148653939-1da48a62-44c3-429c-b99f-6095d0efc3e4.png">
  </p>
    
  __blue box - Enter the terminal.__        
  __yellow box - The command to write.__ <br/>
  __red box - run Ex4 class.__ <br/>
            
  - If you would like to exit the program before it ends,
  just press the "exit" button at the left upper corner of the window. 

# Appearance
<p align="center">
<img src="https://user-images.githubusercontent.com/93203695/148652088-2d8a0089-c7c9-486a-a446-a8380a03fc75.png">
</p>

## You can see detailed information about the appearance of the project at the Wiki:
https://github.com/ArielZidon/Pokemon_Game/wiki/Visualization#a-short-video-of-the-game-running

# Our Scores On The cases 0 - 15

# Computer specifications:
__The program ran on computer type:__ Lenovo ThinkPad T450 Ultrabook Laptop

__Operating System:__ Edition Windows 10 Pro Version 20H2 Installed on ‎4/‎19/‎2021 OS build 19042.1415 Experience Windows Feature Experience Pack 120.2212.3920.0

__Processor model:__ Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz 2.30 GHz

__Installer RAM :__ 16.0 GB (15.8 GB usable)
